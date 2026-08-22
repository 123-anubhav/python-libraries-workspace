import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .sub-title {
        font-size: 18px;
        color: #666666;
        margin-bottom: 30px;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }

    /* Prediction result */
    .prediction-box {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 3px 15px rgba(0,0,0,0.10);
        margin-top: 20px;
    }

    .prediction-title {
        font-size: 20px;
        color: #555555;
    }

    .prediction-price {
        font-size: 40px;
        font-weight: 700;
        color: #1f77b4;
    }

    /* Section heading */
    .section-title {
        font-size: 28px;
        font-weight: 600;
        margin-top: 20px;
        margin-bottom: 15px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATASET
# ============================================================

@st.cache_data
def load_data():

    if not os.path.exists("houses.csv"):
        return None

    df = pd.read_csv("houses.csv")

    return df


df = load_data()


# ============================================================
# CHECK DATASET
# ============================================================

if df is None:

    st.error(
        "❌ houses.csv not found. "
        "Please make sure houses.csv exists in the project folder."
    )

    st.stop()


# ============================================================
# TRAIN MODEL
# ============================================================

@st.cache_resource
def train_model(df):

    # Independent variables
    X = df[
        [
            "area",
            "bedrooms",
            "bathrooms",
            "age"
        ]
    ]

    # Dependent variable
    y = df["price"]

    # Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Create Linear Regression model
    model = LinearRegression()

    # Train model
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation
    mae = mean_absolute_error(y_test, y_pred)

    mse = mean_squared_error(y_test, y_pred)

    rmse = np.sqrt(mse)

    r2 = r2_score(y_test, y_pred)

    return (
        model,
        X_train,
        X_test,
        y_train,
        y_test,
        y_pred,
        mae,
        mse,
        rmse,
        r2
    )


(
    model,
    X_train,
    X_test,
    y_train,
    y_test,
    y_pred,
    mae,
    mse,
    rmse,
    r2
) = train_model(df)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🏠 House Price ML")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📊 Dataset & EDA",
        "🤖 Model Training",
        "📈 Model Evaluation",
        "🔮 Price Prediction"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Machine Learning Model**

    Linear Regression

    Features:
    - Area
    - Bedrooms
    - Bathrooms
    - Age

    Target:
    - Price
    """
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="main-title">🏠 House Price Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Machine Learning application using Linear Regression'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🏘️ Houses",
            len(df)
        )

    with col2:
        st.metric(
            "📊 Features",
            4
        )

    with col3:
        st.metric(
            "🎯 R² Score",
            f"{r2:.4f}"
        )

    with col4:
        st.metric(
            "📉 RMSE",
            f"₹{rmse:,.0f}"
        )

    st.markdown("---")

    # --------------------------------------------------------
    # DATASET PREVIEW
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">📋 Dataset Preview</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    # --------------------------------------------------------
    # QUICK GRAPH
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">📊 Area vs House Price</div>',
        unsafe_allow_html=True
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.scatter(
        df["area"],
        df["price"]
    )

    ax.set_xlabel("Area (sq ft)")

    ax.set_ylabel("Price")

    ax.set_title("Area vs House Price")

    st.pyplot(fig)


# ============================================================
# DATASET & EDA
# ============================================================

elif page == "📊 Dataset & EDA":

    st.title("📊 Dataset & Exploratory Data Analysis")

    st.markdown(
        "Understand the dataset before training the machine learning model."
    )

    # Dataset information

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Rows",
            df.shape[0]
        )

    with col2:
        st.metric(
            "Columns",
            df.shape[1]
        )

    with col3:
        st.metric(
            "Duplicate Rows",
            df.duplicated().sum()
        )

    st.markdown("---")

    # Dataset

    st.subheader("📋 Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )

    # Missing values

    st.subheader("🔍 Missing Values")

    missing = df.isnull().sum()

    missing_df = pd.DataFrame({
        "Column": missing.index,
        "Missing Values": missing.values
    })

    st.dataframe(
        missing_df,
        use_container_width=True
    )

    # Statistics

    st.subheader("📈 Statistical Summary")

    st.dataframe(
        df.describe(),
        use_container_width=True
    )

    # Correlation

    st.subheader("🔥 Correlation Heatmap")

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)

    # Area vs price

    st.subheader("🏠 Area vs Price")

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    sns.scatterplot(
        data=df,
        x="area",
        y="price",
        s=100,
        ax=ax
    )

    ax.set_title(
        "Relationship Between Area and House Price"
    )

    st.pyplot(fig)


# ============================================================
# MODEL TRAINING
# ============================================================

elif page == "🤖 Model Training":

    st.title("🤖 Linear Regression Model Training")

    st.markdown(
        "This section shows how the machine learning model is trained."
    )

    # Features

    st.subheader("1️⃣ Independent Variables (X)")

    st.code(
        """
X = [
    area,
    bedrooms,
    bathrooms,
    age
]
        """
    )

    st.dataframe(
        X_train,
        use_container_width=True
    )

    st.subheader("2️⃣ Dependent Variable (Y)")

    st.code(
        """
Y = price
        """
    )

    st.dataframe(
        y_train.to_frame(),
        use_container_width=True
    )

    # Split

    st.subheader("3️⃣ Train/Test Split")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Training Records",
            len(X_train)
        )

    with col2:

        st.metric(
            "Testing Records",
            len(X_test)
        )

    # Model

    st.subheader("4️⃣ Linear Regression Model")

    st.code(
        """
model = LinearRegression()

model.fit(X_train, y_train)
        """,
        language="python"
    )

    # Coefficients

    st.subheader("5️⃣ Model Coefficients")

    coefficient_df = pd.DataFrame({
        "Feature": X_train.columns,
        "Coefficient": model.coef_
    })

    st.dataframe(
        coefficient_df,
        use_container_width=True
    )

    st.write(
        "Intercept:",
        model.intercept_
    )


# ============================================================
# MODEL EVALUATION
# ============================================================

elif page == "📈 Model Evaluation":

    st.title("📈 Model Evaluation")

    st.markdown(
        "Evaluate how well the Linear Regression model performs."
    )

    # Metrics

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "MAE",
            f"₹{mae:,.2f}"
        )

    with col2:

        st.metric(
            "MSE",
            f"{mse:,.2f}"
        )

    with col3:

        st.metric(
            "RMSE",
            f"₹{rmse:,.2f}"
        )

    with col4:

        st.metric(
            "R² Score",
            f"{r2:.4f}"
        )

    st.markdown("---")

    # Actual vs predicted

    st.subheader(
        "🎯 Actual Price vs Predicted Price"
    )

    result_df = pd.DataFrame({
        "Actual Price": y_test.values,
        "Predicted Price": y_pred
    })

    st.dataframe(
        result_df,
        use_container_width=True
    )

    # Graph

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.scatter(
        y_test,
        y_pred
    )

    ax.set_xlabel(
        "Actual Price"
    )

    ax.set_ylabel(
        "Predicted Price"
    )

    ax.set_title(
        "Actual vs Predicted House Price"
    )

    st.pyplot(fig)


# ============================================================
# PRICE PREDICTION
# ============================================================

elif page == "🔮 Price Prediction":

    st.title("🔮 House Price Prediction")

    st.markdown(
        "Enter house details and let the trained ML model predict the price."
    )

    st.markdown("---")

    # Input columns

    col1, col2 = st.columns(2)

    with col1:

        area = st.number_input(
            "🏠 Area (sq ft)",
            min_value=100,
            max_value=10000,
            value=2500,
            step=100
        )

        bedrooms = st.number_input(
            "🛏️ Bedrooms",
            min_value=1,
            max_value=10,
            value=4,
            step=1
        )

    with col2:

        bathrooms = st.number_input(
            "🚿 Bathrooms",
            min_value=1,
            max_value=10,
            value=3,
            step=1
        )

        age = st.number_input(
            "📅 House Age",
            min_value=0,
            max_value=100,
            value=3,
            step=1
        )

    st.markdown("")

    # Prediction button

    if st.button(
        "🔮 Predict House Price",
        use_container_width=True
    ):

        # Create new house dataframe

        new_house = pd.DataFrame({
            "area": [area],
            "bedrooms": [bedrooms],
            "bathrooms": [bathrooms],
            "age": [age]
        })

        # Prediction

        predicted_price = model.predict(
            new_house
        )[0]

        # Result

        st.markdown(
            f"""
            <div class="prediction-box">

                <div class="prediction-title">
                    Estimated House Price
                </div>

                <div class="prediction-price">
                    ₹{predicted_price:,.2f}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.subheader("🏠 Input Details")

        result_input = pd.DataFrame({
            "Area": [area],
            "Bedrooms": [bedrooms],
            "Bathrooms": [bathrooms],
            "Age": [age]
        })

        st.dataframe(
            result_input,
            use_container_width=True
        )


# ============================================================
# FOOTER
# ============================================================

st.sidebar.markdown("---")

st.sidebar.caption(
    "Linear Regression ML Project | Streamlit"
)