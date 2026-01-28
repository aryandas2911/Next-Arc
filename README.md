# 🎬 Next Arc — Anime Recommender System

**Next Arc** is a content-based anime recommendation system that helps users discover new anime based on what they already enjoy. The system analyzes anime metadata such as **genres, tags, and themes** to identify similarities between titles and generate meaningful recommendations.

The project applies **TF-IDF vectorization** and **cosine similarity** to model content relationships and is delivered through an **interactive Streamlit web interface**, making anime discovery intuitive, fast, and engaging.

---

## 🧠 How It Works (Recommendation Logic)

1. **Data Collection**  
   The system uses an anime dataset containing metadata like titles, genres, tags, and themes.

2. **Text Processing & Feature Extraction**  
   Metadata fields are combined and transformed into numerical vectors using **TF-IDF (Term Frequency–Inverse Document Frequency)** to capture the importance of each term across all anime.

3. **Similarity Calculation**  
   **Cosine similarity** is computed between anime vectors to measure how closely related each title is to the others.

4. **Recommendation Generation**  
   Given a selected anime, the system ranks all other titles by similarity scores and returns the top matches as personalized recommendations.

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Libraries:** 
  - `pandas`, `numpy` — data manipulation  
  - `scikit-learn` — TF-IDF vectorization & cosine similarity  
  - `streamlit` — interactive web interface  
  - `pickle` — saving and loading preprocessed data
- **Frontend:** Streamlit for quick, responsive UI  
- **Data:** Kaggle Anime Dataset (metadata including genres, tags, themes) `https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset`

---

## 🚀 Usage / How to Run

1. **Clone the repository**  
```bash
git clone https://github.com/aryandas2911/Next-Arc
cd next-arc
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app
```bash
streamlit run app.py
```

4. Interact with the app
- Select an anime you’ve watched
- Get a ranked list of recommended anime based on content similarity
- Explore new anime with their metadata

---

## 🔮 Future Improvements / Roadmap

- **Dynamic Data Updates**: Automatically fetch new anime and update the dataset without manual preprocessing.  
- **Enhanced Features**: Include more metadata such as ratings, studios, and user reviews to improve recommendation quality.  
- **Hybrid Recommendation**: Combine content-based filtering with collaborative filtering for personalized recommendations.  
- **Deployment Enhancements**: Containerize the app using Docker or deploy on cloud platforms like Render or Heroku for better scalability.  
- **Performance Optimization**: Use sparse matrices or approximate nearest neighbor search to handle larger datasets efficiently.
