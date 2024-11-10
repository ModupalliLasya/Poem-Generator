from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import torch

tokenizer = GPT2TokenizerFast.from_pretrained('saved_model/')
model = GPT2LMHeadModel.from_pretrained('saved_model/')

def generate_poem(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=500,
        num_beams=5,
        no_repeat_ngram_size=2,
        pad_token_id=tokenizer.eos_token_id, 
        early_stopping=True
    )
    poem = tokenizer.decode(output[0], skip_special_tokens=True)
    poem_with_linebreaks = poem.replace("\n", "<br>")

    return poem_with_linebreaks
