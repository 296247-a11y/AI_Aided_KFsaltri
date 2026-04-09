import json
import matplotlib.pyplot as plt

# Load the JSON data
file_path = "./log/LorenzSSM_danse_opt_gru_m_3_n_3_T_100_N_1000_sigmae2_-10.0dB_smnr_10.0dB/danse_gru_losses_eps2000.json"
with open(file_path, "r") as file:
    data = json.load(file)

# Extract training and validation losses
tr_losses = data["tr_losses"]
val_losses = data["val_losses"]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(tr_losses, label="Training Loss", color="blue")
plt.plot(val_losses, label="Validation Loss", color="orange")
plt.title("Training and Validation Losses")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Save the plot
output_file = "danse_gru_losses_plot.png"
plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.show()

print(f"Plot saved as {output_file}")
