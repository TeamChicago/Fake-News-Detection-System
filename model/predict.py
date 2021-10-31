from transformers import BertTokenizer, BertForSequenceClassification
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

model = BertForSequenceClassification.from_pretrained("bert-base-uncased")
model.config.num_labels = 1

for param in model.parameters():
    param.requires_grad = False

model.classifier = nn.Sequential(
    nn.Linear(768, 256),
    nn.LeakyReLU(),
    nn.Linear(256,64),
    nn.LeakyReLU(),
    nn.Linear(64, 2),
    nn.Softmax(dim=1)
)
model = model.to(device)

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

class Predictor:
    def preprocess_text(self, text):
        parts = []

        text_len = len(text.split(' '))
        max_parts = 5
        nb_cuts = int(text_len / 300)
        nb_cuts = min(nb_cuts, max_parts)
        
        
        for i in range(nb_cuts + 1):
            text_part = ' '.join(text.split(' ')[i * 300: (i + 1) * 300])
            parts.append(tokenizer.encode(text_part, return_tensors="pt", max_length=500).to(device))

        return parts

    def predictor(self, text):
        RT = self.preprocess_text(text)
        overall_output = torch.zeros((1,2)).to(device)

        for part in RT:
            if len(part) > 0:
                overall_output += model(part.reshape(1, -1))[0]
            
        overall_output = F.softmax(overall_output[0], dim=-1)
        result = overall_output[0].float().item() * 100

        return result