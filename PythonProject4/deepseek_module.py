# deepseek_module.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class DeepResponder:
    def __init__(self, model_name="deepseek-ai/deepseek-coder-6.7b-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        self.model.eval()

    def generate(self, prompt, max_length=150):
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        output = self.model.generate(
            input_ids,
            max_length=max_length,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            repetition_penalty=1.2,
            pad_token_id=self.tokenizer.eos_token_id
        )
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

# Пример использования
if __name__ == "__main__":
    responder = DeepResponder()
    print(responder.generate("Объясни, как работает нейросеть Transformer."))