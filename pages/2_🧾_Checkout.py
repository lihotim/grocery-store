import streamlit as st


# @_@ add process order logic here, e.g.:
# update DB, print receipt, set "selected_items" to all 0, go back to homepage
def process_order():
    print("Checkout button pressed! Your order is being processed.")


st.title("Checkout page")
st.write("---")

# st.write(f"#_# session_state: ")
# st.write(f"{st.session_state}")

if "selected_items" not in st.session_state or len(st.session_state["selected_items"]) == 0:
    st.subheader("No items added yet!")
    st.markdown('<a href="/" target="_self">Home page</a>',
                unsafe_allow_html=True)
else:
    selected_items = st.session_state["selected_items"]
    st.write(f"@_@ selected_items: ")
    for item in selected_items:
        st.write(str(item))

    st.write("---")

    for item in selected_items:

        # Create two columns with a ratio of 1:3
        col1, col2, col3 = st.columns([1, 3, 1])

        # Column 1: Image
        with col1:
            st.image(item["image"], use_column_width=True)

        # Column 2: item details
        with col2:
            st.write(f"Item: {item['name']}")
            st.write(f"Unit Price: ${item['price']:.2f}")
            # st.write(f"Quantity: {item['quantity']}")

        # Column 3: Add, Minus, Remove
        with col3:
            # Get the current quantity from the session state
            quantity = item['quantity']

            # Calculate sub total
            sub_total = item['price'] * quantity
            st.write(f"Sub total: ${sub_total:.2f}")

    st.write("---")

    # Calculate the total price
    total_price = sum(item['quantity'] * item['price']
                      for item in selected_items)

    # Display the total price in the last row
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        st.markdown(f"**Total Price:**")

    with col2:
        st.write(" ")

    with col3:
        st.markdown(f"**${total_price:.2f}**", unsafe_allow_html=True)
        if st.button("CHECKOUT"):
            process_order()
