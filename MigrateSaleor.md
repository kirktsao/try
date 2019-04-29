All csv.files should under server /tmp/
product_products:

copy public.product_product (id, name, description, price, available_on, updated_at, product_type_id, attributes, is_published, category_id, seo_description, seo_title, charge_taxes, tax_rate, weight) FROM '/tmp/p1.csv' CSV HEADER DELIMITER ',' FORCE NOT NULL attributes;




product_productvariant:
copy public.product_productvariant (id, sku, name, price_override, product_id, attributes, cost_price, quantity, quantity_allocated, track_inventory, weight) FROM '/tmp/p2.csv' CSV HEADER FORCE NOT NULL name,attributes ;


product_productsimage:
copy public.product_productimage (id, image, ppoi, alt, sort_order, product_id) FROM '/tmp/p3.csv' CSV HEADER DELIMITER ',' FORCE NOT NULL alt;



Update Attribute
update public.product_product set attributes = attributes || '"1"=>"1"'::hstore where id > 182;