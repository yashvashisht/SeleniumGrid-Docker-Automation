"""
PARALLEL TEST RUNNER WITH COMPREHENSIVE LOGGING
Logs all test results to file for detailed reporting
"""

import multiprocessing
import time
from datetime import datetime
from pathlib import Path

# Import all test functions
from test_facebook import test_facebook
from test_google import test_google
from test_wikipedia import test_wikipedia
from test_github import test_github
from test_linkedin import test_linkedin


def setup_logging(log_dir="test_logs"):
    """Create log directory and file with sequential numbering"""
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True)
    
    # Find the next sequence number
    existing_logs = list(log_path.glob("test_run_*.log"))
    next_num = len(existing_logs) + 1
    
    # Format timestamp as: 2026-03-17_16-43-14
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Format: test_run_001_2026-03-17_16-43-14.log
    return log_path, timestamp, f"{next_num:03d}"


def log_message(file_obj, message, console=True):
    """Write message to log file and optionally to console"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}\n"
    file_obj.write(log_line)
    if console:
        print(message)
    file_obj.flush()


def run_test_with_logging(test_info):
    """Run a single test and return results"""
    test_func, test_name = test_info
    
    start_time = time.time()
    status = "PASS"
    error_msg = None
    
    try:
        test_func()
    except Exception as e:
        status = "FAIL"
        error_msg = str(e)
    
    duration = time.time() - start_time
    
    return {
        'test_name': test_name,
        'status': status,
        'duration': duration,
        'error': error_msg
    }


def main():
    # Setup logging
    log_dir, timestamp, seq_num = setup_logging()
    log_file_path = log_dir / f"test_run_{seq_num}_{timestamp}.log"
    
    # Open single comprehensive log
    with open(log_file_path, 'w', encoding='utf-8') as log_file:
        # Header
        log_message(log_file, "=" * 70)
        log_message(log_file, "SELENIUM GRID - PARALLEL TEST EXECUTION REPORT")
        log_message(log_file, "=" * 70)
        log_message(log_file, f"Test Run ID: {timestamp}")
        log_message(log_file, f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        log_message(log_file, "")
        
        # Test list
        tests = [
            (test_facebook, "Facebook Login Test"),
            (test_google, "Google Search Test"),
            (test_wikipedia, "Wikipedia Navigation Test"),
            (test_github, "GitHub Navigation Test"),
            (test_linkedin, "LinkedIn Navigation Test")
        ]
        
        log_message(log_file, f"Scheduled Tests ({len(tests)}):")
        for _, test_name in tests:
            log_message(log_file, f"  • {test_name}")
        
        log_message(log_file, "")
        log_message(log_file, "Starting parallel execution...")
        log_message(log_file, "=" * 70)
        log_message(log_file, "")
        
        # Run tests in parallel using multiprocessing
        start_time = time.time()
        
        with multiprocessing.Pool(processes=len(tests)) as pool:
            results = pool.map(run_test_with_logging, tests)
        
        total_time = time.time() - start_time
        
        # Log results
        log_message(log_file, "")
        log_message(log_file, "TEST RESULTS:")
        log_message(log_file, "-" * 70)
        
        passed_count = 0
        failed_count = 0
        
        for result in results:
            test_name = result['test_name']
            status = result['status']
            duration = result['duration']
            error = result['error']
            
            status_emoji = "✓" if status == "PASS" else "✗"
            log_message(log_file, f"{status_emoji} {test_name:<35} {status:<8} {duration:>6.2f}s")
            
            if error:
                log_message(log_file, f"  Error: {error}")
            
            if status == "PASS":
                passed_count += 1
            else:
                failed_count += 1
        
        log_message(log_file, "-" * 70)
        log_message(log_file, "")
        
        # Summary statistics
        log_message(log_file, "SUMMARY STATISTICS:")
        log_message(log_file, "-" * 70)
        log_message(log_file, f"Total Tests Run: {len(results)}")
        log_message(log_file, f"Passed: {passed_count} ({passed_count/len(results)*100:.1f}%)")
        log_message(log_file, f"Failed: {failed_count} ({failed_count/len(results)*100:.1f}%)")
        log_message(log_file, f"Total Duration: {total_time:.2f}s")
        log_message(log_file, f"Average Duration: {total_time/len(results):.2f}s")
        
        # Parallel speedup calculation
        sequential_time = sum(r['duration'] for r in results) * len(results)
        speedup = sequential_time / total_time if total_time > 0 else 0
        
        log_message(log_file, "")
        log_message(log_file, "PARALLEL SPEEDUP ANALYSIS:")
        log_message(log_file, "-" * 70)
        log_message(log_file, f"Sequential execution (one test at a time): {sequential_time:.2f}s")
        log_message(log_file, f"Parallel execution (all tests together): {total_time:.2f}s")
        log_message(log_file, f"Speedup factor: {speedup:.1f}x faster")
        
        log_message(log_file, "")
        log_message(log_file, "=" * 70)
        log_message(log_file, f"Test Run Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        log_message(log_file, "=" * 70)
    
    # Print console output
    print("\n" + "=" * 70)
    print("✓ TEST EXECUTION COMPLETED")
    print("=" * 70)
    print(f"\nResults Summary:")
    print(f"  Total Tests: {len(results)}")
    print(f"  Passed: {passed_count}")
    print(f"  Failed: {failed_count}")
    print(f"  Total Time: {total_time:.2f}s")
    print(f"  Speedup: {speedup:.1f}x faster\n")
    
    print(f"Log File:")
    print(f"  📋 {log_file_path}\n")


if __name__ == "__main__":
    main()
