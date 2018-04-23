// Add a custom product setting tab to edit product pages options FOR SIMPLE PRODUCTS only
add_filter( 'woocommerce_product_data_tabs', 'discount_new_product_data_tab', 50, 1 );
function discount_new_product_data_tab( $tabs ) {
    $tabs['discount'] = array(
        'label' => __( 'Discount', 'woocommerce' ),
        'target' => 'discount_product_data', // <== to be used in the <div> class of the content
        'class' => array('show_if_simple'), // or 'hide_if_simple' or 'show_if_variable'…
    );

    return $tabs;
}

// Add/display custom Fields in the custom product settings tab
add_action( 'woocommerce_product_data_panels', 'add_custom_fields_product_options_discount', 10 );
function add_custom_fields_product_options_discount() {
    global $post;

    echo '<div id="discount_product_data" class="panel woocommerce_options_panel">'; // <== Here we use the target attribute

    woocommerce_wp_text_input(  array(
        'type'          => 'number', // Add an input number Field
        'id'            => '_discount_info',
        'label'         => __( 'Percentage Discount', 'woocommerce' ),
        'placeholder'   => __( 'Enter the % discount.', 'woocommerce' ),
        'description'   => __( 'Explanations about the field info discount.', 'woocommerce' ),
        'desc_tip'      => 'true',
        'custom_attributes' => array(
            'step' => 'any',
            'min' => '1'
        ),
    ) );

    echo '</div>';
}

// Save the data value from the custom fields for simple products
add_action( 'woocommerce_process_product_meta_simple', 'save_custom_fields_product_options_discount', 50, 1 );
function save_custom_fields_product_options_discount( $post_id ) {
    // Save Number Field value
    $number_field = $_POST['_discount_info'];

    if( ! empty( $number_field ) ) {
        update_post_meta( $post_id, '_discount_info', esc_attr( $number_field ) );
    }
}
