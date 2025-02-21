import streamlit as st
from products import products
from utils import load_css, get_filtered_products
from checkout import show_checkout_form
from auth import show_login, show_profile

# Load custom CSS for enhanced UI
load_css()

# Initialize session states
def initialize_session_states():
    session_defaults = {
        "authenticated": False,
        "cart": [],
        "wishlist": [],
        "current_page": "🏠 Home",
        "selected_product": None,
        "dark_mode": False
    }
    
    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

initialize_session_states()

# Dark Mode Toggle
def toggle_dark_mode():
    if st.sidebar.button("🌓 Toggle Dark Mode"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

# Apply Dark Mode Styling
def apply_dark_mode():
    if st.session_state.dark_mode:
        st.markdown("""
            <style>
                body {
                    background: #0B0C10;
                    color: #F0F0F0;
                }
                .stButton>button {
                    background: linear-gradient(145deg, #6C5B7B, #0B0C10);
                    color: #F0F0F0;
                }
                .stTextInput>div>div>input {
                    background: rgba(0, 0, 0, 0.3);
                    color: #F0F0F0;
                }
                .glass-panel {
                    background: rgba(0, 0, 0, 0.3);
                }
                .data-card {
                    background: rgba(0, 0, 0, 0.3);
                }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                body {
                    background: radial-gradient(circle, #0B0C10 0%, #000 100%);
                    color: #F0F0F0;
                }
                .stButton>button {
                    background: linear-gradient(145deg, #6C5B7B, #0B0C10);
                    color: #F0F0F0;
                }
                .stTextInput>div>div>input {
                    background: rgba(0, 0, 0, 0.3);
                    color: #F0F0F0;
                }
                .glass-panel {
                    background: rgba(255, 255, 255, 0.1);
                }
                .data-card {
                    background: rgba(255, 255, 255, 0.1);
                }
            </style>
        """, unsafe_allow_html=True)

# Sidebar Navigation
def setup_sidebar():
    st.sidebar.header("🔗 Navigation")
    pages = ["🏠 Home", "📦 Product Details", "🛒 Cart", "❤️ Wishlist", "💳 Checkout", "🔑 Login"]
    st.session_state.current_page = st.sidebar.radio("Go to", pages)
    show_profile()

# Handle authentication
def check_authentication():
    if not st.session_state.authenticated and st.session_state.current_page != "🔑 Login":
        show_login()
        st.stop()

# Product Filtering and Sorting
def get_product_filters():
    search_query = st.sidebar.text_input("🔍 Search Products", "")
    category_filter = st.sidebar.selectbox(
        "📂 Filter by Category", 
        ["All"] + list(set(p["category"] for p in products))
    )
    sort_option = st.sidebar.selectbox(
        "📊 Sort By", 
        ["Price: Low to High", "Price: High to Low", "Rating", "Newest"]
    )
    return search_query, category_filter, sort_option

def sort_products(products, sort_option):
    if sort_option == "Price: Low to High":
        return sorted(products, key=lambda x: x["price"])
    elif sort_option == "Price: High to Low":
        return sorted(products, key=lambda x: x["price"], reverse=True)
    elif sort_option == "Rating":
        return sorted(products, key=lambda x: x.get("rating", 0), reverse=True)
    return products

# Product Display
def display_product_card(product, col):
    with col:
        st.image(product.get("image", "https://via.placeholder.com/150"), width=150)
        st.subheader(product["name"])
        st.write(f"💲 Price: ${product['price']:.2f}")
        st.write(f"⭐ {product.get('rating', 'No Rating')} / 5")

        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"📄 Details - {product['name']}", key=f"details_{product['name']}"):
                st.session_state.selected_product = product
                st.session_state.current_page = "📦 Product Details"
                st.rerun()
        with col2:
            if st.button(f"🛒 Add - {product['name']}", key=f"add_{product['name']}"):
                st.session_state.cart.append(product)
                st.success(f"{product['name']} added to cart!")

def show_products():
    st.header("📦 Products")
    search_query, category_filter, sort_option = get_product_filters()
    
    filtered_products = get_filtered_products(
        products, search_query, category_filter, 0, float("inf")
    )
    sorted_products = sort_products(filtered_products, sort_option)
    
    cols = st.columns(3)
    for idx, product in enumerate(sorted_products):
        display_product_card(product, cols[idx % 3])

# Product Details
def show_product_details():
    product = st.session_state.selected_product
    if not product:
        st.error("No product selected.")
        return

    st.image(product.get("image", "https://via.placeholder.com/300"), width=300)
    st.subheader(product["name"])
    st.write(f"💲 Price: ${product['price']:.2f}")
    st.write(f"📂 Category: {product['category']}")
    st.write(f"⭐ Rating: {product.get('rating', 'No Rating')} / 5")
    st.write(product.get("description", "No description available."))

    if "features" in product:
        st.subheader("🔹 Features")
        for feature in product["features"]:
            st.write(f"- {feature}")

    if "specs" in product:
        st.subheader("🔧 Specifications")
        for key, value in product["specs"].items():
            st.write(f"**{key}:** {value}")

    if "reviews" in product:
        st.subheader("📝 Reviews")
        for review in product["reviews"]:
            st.write(f"**{review['user']}** ({review['rating']}/5): {review['comment']}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🛒 Add to Cart"):
            st.session_state.cart.append(product)
            st.success(f"{product['name']} added to cart!")
    with col2:
        if st.button("❤️ Add to Wishlist"):
            st.session_state.wishlist.append(product)
            st.success(f"{product['name']} added to wishlist!")

# Wishlist
def show_wishlist():
    st.header("❤️ Wishlist")
    if not st.session_state.wishlist:
        st.write("Your wishlist is empty.")
        return
    
    for item in st.session_state.wishlist:
        st.write(f"- {item['name']} - ${item['price']:.2f}")
        if st.button(f"🛒 Move to Cart - {item['name']}", key=f"wishlist_{item['name']}"):
            st.session_state.cart.append(item)
            st.session_state.wishlist.remove(item)
            st.success(f"{item['name']} moved to cart!")
            st.rerun()

# Cart
def show_cart():
    st.header("🛒 Cart")
    if not st.session_state.cart:
        st.write("Your cart is empty.")
        return

    total_price = sum(p["price"] for p in st.session_state.cart)
    for item in st.session_state.cart:
        st.image(item.get("image", "https://via.placeholder.com/100"), width=100)
        st.write(f"- {item['name']} - ${item['price']:.2f}")
        if st.button(f"❌ Remove {item['name']}", key=f"remove_{item['name']}"):
            st.session_state.cart.remove(item)
            st.rerun()

    st.write(f"**Total: ${total_price:.2f}**")
    if st.button("💳 Proceed to Checkout"):
        st.session_state.current_page = "💳 Checkout"
        st.rerun()

# Checkout
def show_checkout():
    st.header("💳 Checkout")
    if not st.session_state.cart:
        st.write("Your cart is empty. Add products before checking out!")
        return
    show_checkout_form()

# Main Application
def main():
    toggle_dark_mode()
    apply_dark_mode()
    setup_sidebar()
    check_authentication()

    page_handlers = {
        "🏠 Home": show_products,
        "📦 Product Details": show_product_details,
        "🛒 Cart": show_cart,
        "❤️ Wishlist": show_wishlist,
        "💳 Checkout": show_checkout,
        "🔑 Login": show_login
    }

    page_handlers[st.session_state.current_page]()

if __name__ == "__main__":
    main()
def display_product_card(product, col):
    with col:
        # Card container with hover effect
        with st.container():
            # Image with fixed aspect ratio
            st.image(
                product.get("image", "https://via.placeholder.com/300"),
                use_column_width=True,
                output_format="auto"
            )
            
            # Product name and category
            st.markdown(f"**{product['name']}**")
            st.caption(f"📂 {product['category']}")
            
            # Price and discount
            original_price = product.get("original_price", product["price"])
            if original_price != product["price"]:
                st.markdown(f"""
                    <span style="text-decoration: line-through; color: #888;">${original_price:.2f}</span>
                    <span style="color: var(--meteor-orange);">${product['price']:.2f}</span>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"💲 **${product['price']:.2f}**")
            
            # Rating with stars
            rating = product.get("rating", 0)
            stars = "⭐" * int(rating) + "☆" * (5 - int(rating))
            st.markdown(f"{stars} ({rating}/5)")
            
            # Quick actions
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button(f"📄 Details", key=f"details_{product['id']}"):
                    st.session_state.selected_product = product
                    st.session_state.current_page = "📦 Product Details"
                    st.rerun()
            with col2:
                if st.button(f"🛒 Add", key=f"add_{product['id']}"):
                    st.session_state.cart.append(product)
                    st.success(f"{product['name']} added to cart!")
            
            # Additional info
            with st.expander("More Info"):
                if "features" in product:
                    st.write("**Features:**")
                    for feature in product["features"]:
                        st.write(f"- {feature}")
                if "specs" in product:
                    st.write("**Specifications:**")
                    for key, value in product["specs"].items():
                        st.write(f"**{key}:** {value}")

def show_products():
    st.header("📦 Products")
    
    # Filters
    search_query, category_filter, sort_option = get_product_filters()
    
    # Apply filters and sorting
    filtered_products = get_filtered_products(
        products, search_query, category_filter, 0, float("inf")
    )
    sorted_products = sort_products(filtered_products, sort_option)
    
    # Responsive grid layout
    cols = st.columns(3)
    for idx, product in enumerate(sorted_products):
        display_product_card(product, cols[idx % 3])
        
        # Create new row after every 3 products
        if (idx + 1) % 3 == 0 and (idx + 1) < len(sorted_products):
            cols = st.columns(3)