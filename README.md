# letter_counting_lora_project.zip
The submission includes code that applies LoRA (e.g., via PEFT) to the chosen base LLM. LoRA hyperparameters are explicitly set and valid `lora_rank` one of 8, 16, 32, 64, 128 target modules includes `q_proj`, `k_proj`, `v_proj`, `o_proj` and/or `gate_proj`, `up_proj`, `down_proj` The configuration is used to successfully instantiate a trainable.
