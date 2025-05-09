from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

class BiharChatModel:
    def __init__(self):
        self.model_name = "gpt2"  # Using GPT-2 as primary for reliability
        self.model = None
        self.tokenizer = None
        self.initialize_model()
        
    def initialize_model(self):
        """Initialize model with multiple fallback options"""
        try:
            # Try loading GPT-2 first
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.model_name,
                local_files_only=True  # Use cached version if available
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                torch_dtype=torch.float32,
                device_map="auto"
            )
        except Exception as e:
            print(f"Error loading model: {e}")
            self.load_basic_model()
    
    def load_basic_model(self):
        """Final fallback to a very basic model"""
        from transformers import GPT2Tokenizer, GPT2LMHeadModel
        try:
            self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
            self.model = GPT2LMHeadModel.from_pretrained('gpt2')
        except Exception as e:
            print(f"Critical error: {e}")
            self.setup_dummy_model()
    
    def setup_dummy_model(self):
        """Emergency fallback when no models can be loaded"""
        from transformers import GPT2Config
        print("Using dummy model - functionality will be limited")
        config = GPT2Config()
        self.model = GPT2LMHeadModel(config)
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2', add_prefix_space=True)
    
    def generate_response(self, prompt, context=None):
        """Generate response with error handling"""
        if not self.model or not self.tokenizer:
            return "System is initializing. Please try again later."
            
        try:
            input_text = f"Context: {context}\nQuestion: {prompt}\nAnswer:" if context else prompt
            inputs = self.tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_length=200,
                    num_return_sequences=1,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            print(f"Generation error: {e}")
            return f"I encountered an error: {str(e)}. Please try a different question."