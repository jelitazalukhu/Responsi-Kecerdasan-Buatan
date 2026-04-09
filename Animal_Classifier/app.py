import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

class Net(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(32)

        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)

        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.bn3 = nn.BatchNorm2d(128)

        self.pooling = nn.MaxPool2d(2, 2)
        self.relu = nn.ReLU()

        self.dropout = nn.Dropout(0.5)

        self.flatten = nn.Flatten()
        self.linear = nn.Linear(128 * 16 * 16, 128)
        self.output = nn.Linear(128, 3)

    def forward(self, x):
        x = self.pooling(self.relu(self.bn1(self.conv1(x))))
        x = self.pooling(self.relu(self.bn2(self.conv2(x))))
        x = self.pooling(self.relu(self.bn3(self.conv3(x))))

        x = self.flatten(x)
        x = self.relu(self.linear(x))
        x = self.dropout(x)
        x = self.output(x)

        return x


@st.cache_resource
def load_model():
    model = Net()
    model.load_state_dict(torch.load('Animal_Classifier/animal_classifier.pth', map_location=torch.device('cpu')))
    model.eval()
    return model

st.set_page_config(page_title="Animal Classifier", page_icon="🐾")


st.markdown("""
    """, unsafe_allow_html=True)

st.title("Animal Classifier")
st.write("Upload foto anjing, kucing, atau satwa liar untuk diprediksi!")

file = st.file_uploader("", type=['jpg', 'png', 'jpeg'])

if file:
    img = Image.open(file)
    st.image(img, caption="Gambar yang kamu pilih", use_container_width=True)
    
    if st.button("Analisis Sekarang"):
        transform = transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        
        tensor = transform(img.convert('RGB')).unsqueeze(0)
        
        with st.spinner("Model sedang berpikir..."):
            model = load_model()
            output = model(tensor)
            _, pred = torch.max(output, 1)
            
            # GANTI SESUAI URUTAN LABELMU
            labels = ['Kucing', 'Anjing', 'Wild Animal']
            hasil = labels[pred.item()]
            
        
            st.success(f"Hewan ini adalah **{hasil}**!")