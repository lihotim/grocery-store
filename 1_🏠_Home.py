from pathlib import Path
import math

import streamlit as st
from PIL import Image

# to be retrieved from DB
products = [
    {'id': "0", 'name': 'Item #1', 'price': 1.05,
        'image': 'https://placedog.net/300', },
    {'id': "1", 'name': 'Item #2', 'price': 2.05,
        'image': 'https://placedog.net/301', },
    {'id': "2", 'name': 'Item #3', 'price': 3.05,
        'image': 'https://placedog.net/302', },
    {'id': "3", 'name': 'Item #4', 'price': 4.05,
        'image': 'https://placedog.net/303', },
    {'id': "4", 'name': 'Item #5', 'price': 5.05,
        'image': 'https://placedog.net/304', },
    # {'id': "5", 'name': 'Item #6', 'price': 6.05,
    #     'image': 'https://placedog.net/305', },
]

st.set_page_config(
    page_title="Grocery Store App",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="expanded",
)
with st.sidebar:
    # st.success("Select a page above.")
    st.write("Welcome to IKEA store!")


if 'selected_items' not in st.session_state:
    st.session_state['selected_items'] = []
    ids_list = []
else:
    selected_items = st.session_state["selected_items"]
    ids_list = [item['id'] for item in selected_items]
    # st.write(f"ids_list: {ids_list}")

    # st.write(f"@_@ selected_items: ")
    # for item in selected_items:
    #     st.write(str(item))


def get_quantity_by_id(item_id: str):
    for item in st.session_state['selected_items']:
        if item['id'] == item_id:
            return item['quantity']
    return 0


def main():
    st.title("Home")
    # st.header("(Display all items below...)")
    # st.subheader("(Display all items below...)")

    st.write("---")

    PRODUCTS_PER_ROW = 3
    num_products = len(products)
    num_rows = math.ceil(num_products / PRODUCTS_PER_ROW)

    for row in range(num_rows):
        cols = st.columns(PRODUCTS_PER_ROW)
        products_in_this_row = min(
            PRODUCTS_PER_ROW, num_products - row * PRODUCTS_PER_ROW)

        for i in range(products_in_this_row):
            product_id = row * PRODUCTS_PER_ROW + i
            product = products[product_id]
            col = cols[i]

            with col:
                # Load the product image and display product details
                col.write(f"product_id: {product_id}")

                isExist = str(product_id) in ids_list
                # col.write(f"isExist: {isExist}")

                hist_Qty = get_quantity_by_id(str(product_id))
                # col.write(f"hist_Qty: {hist_Qty}")

                col.image(products[product_id]["image"],
                          use_column_width="always")
                col.subheader(product['name'])
                col.write(f"Price: ${product['price']}")

                item_added = False

                # Update selected items and their quantities in the session state dictionary
                # quantity = col.number_input(
                #     "Quantity:", min_value=0, step=1, key=product_id,
                #     value=0)
                quantity = col.number_input(
                    "Quantity:", min_value=0, step=1, key=product_id,
                    value=hist_Qty if isExist else 0)

                # Check if the product is already in the selected_items list
                item_added = False
                for item in st.session_state.selected_items:
                    if item['id'] == product['id']:
                        item_added = True
                        if quantity == 0:
                            # If the quantity is zero, remove the item from the list
                            st.session_state.selected_items.remove(item)
                        else:
                            # Update the quantity of the item
                            item['quantity'] = quantity
                        break

                # If the product is not in the selected_items list and the quantity is greater than zero, add it
                if not item_added and quantity > 0:
                    st.session_state.selected_items.append({
                        'id': product['id'],
                        'name': product['name'],
                        'price': product['price'],
                        'quantity': quantity,
                        'image': product['image'],
                    })

                st.write("---")


if __name__ == '__main__':
    main()
