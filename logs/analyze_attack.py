# analyze_attack.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# -----------------------------------
# Configuration
# -----------------------------------
LOG_FILE = os.path.join("logs", "timing_results.txt")

# -----------------------------------
# Load and Parse Timing Data
# -----------------------------------
def load_timing_data(file_path):
    data = []
    with open(file_path, "r") as f:
        for line in f:
            try:
                ciphertext, time_taken = line.strip().split(',')
                data.append({
                    "ciphertext": ciphertext,
                    "time": float(time_taken)
                })
            except ValueError:
                continue
    return pd.DataFrame(data)

# -----------------------------------
# Visualize Timing
# -----------------------------------
def plot_response_times(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df["time"], marker='o', linestyle='-', color='blue', label='Decryption Time')
    plt.title("RSA Timing Attack - Response Time per Ciphertext")
    plt.xlabel("Test Number")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# -----------------------------------
# Analyze Patterns
# -----------------------------------
def print_statistics(df):
    times = df["time"].tolist()
    print(f"\n📊 Statistics:")
    print(f"- Total tests: {len(times)}")
    print(f"- Average time: {statistics.mean(times):.6f} sec")
    print(f"- Minimum time: {min(times):.6f} sec")
    print(f"- Maximum time: {max(times):.6f} sec")
    print(f"- Standard deviation: {statistics.stdev(times):.6f} sec")

    # Optional: print top 5 slowest
    top_slowest = df.sort_values(by="time", ascending=False).head(5)
    print("\n🔍 Top 5 Slowest Decryptions:")
    for i, row in top_slowest.iterrows():
        print(f"#{i+1} | Time: {row['time']*1000:.3f} ms | Ciphertext Head: {row['ciphertext'][:10]}...")

# -----------------------------------
# Entry Point
# -----------------------------------
if __name__ == "__main__":
    print("✅ analyze_attack.py started...\n")

    if not os.path.exists(LOG_FILE):
        print(f"❌ ERROR: Log file not found at {LOG_FILE}")
        exit(1)

    df = load_timing_data(LOG_FILE)
    if df.empty:
        print("⚠️ No timing data found in the log file.")
        exit(1)

    print(f"✅ Loaded {len(df)} entries from {LOG_FILE}")
    print(df.head())

    
    print_statistics(df)
    plot_response_times(df)
