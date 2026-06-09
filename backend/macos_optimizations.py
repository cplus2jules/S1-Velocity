import os
import sys
import subprocess
from loguru import logger

def disable_malloc_stack_logging():
    """Disable MallocStackLogging to reduce console noise"""
    os.environ['MallocStackLogging'] = '0'
    os.environ['MallocStackLoggingNoCompact'] = '1'
    logger.debug("   MallocStackLogging disabled")

def optimize_macos_memory():
    """Apply macOS-specific memory optimizations"""
    os.environ['MallocScribble'] = '0'
    os.environ['MallocPreScribble'] = '0'
    os.environ['MallocGuardEdges'] = '0'
    logger.debug("   MacOS memory debugging disabled")

def optimize_for_m1_air():
    """Apply M1 MacBook Air specific optimizations"""
    # M1 Air has 4 performance + 4 efficiency cores. 
    # Use only performance cores for inference.
    os.environ['OMP_NUM_THREADS'] = '4'
    os.environ['MKL_NUM_THREADS'] = '4'
    os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
    os.environ['PYTORCH_MPS_HIGH_WATERMARK_RATIO'] = '0.0'
    logger.info("[OK] M1 Air optimized threading and MPS fallback enabled")

def check_thermal_state():
    """Check macOS thermal state to warn about throttling"""
    try:
        # Check for CPU speed limit in thermal log
        result = subprocess.run(['pmset', '-g', 'thermlog'], capture_output=True, text=True, timeout=2)
        if 'CPU_Speed_Limit' in result.stdout:
            # Check if it's below 100%
            import re
            match = re.search(r'CPU_Speed_Limit\s+=\s+(\d+)', result.stdout)
            if match and int(match.group(1)) < 100:
                logger.warning(f"⚠️  Thermal throttling detected: CPU Speed Limit {match.group(1)}%")
                return True
    except Exception as e:
        logger.debug(f"   Could not check thermal state: {e}")
    return False

def apply_all_optimizations():
    """Apply all macOS-specific optimizations"""
    logger.info("🍎 Applying macOS-specific optimizations...")
    
    disable_malloc_stack_logging()
    optimize_macos_memory()
    
    # Detect Apple Silicon
    import platform
    if platform.system() == "Darwin" and platform.machine() == "arm64":
        optimize_for_m1_air()
        
    # Check thermal state once at startup
    check_thermal_state()
    
    logger.info("[OK] All macOS optimizations applied")

if __name__ == "__main__":
    apply_all_optimizations()
