All csv.files should under server /tmp/
product_products:

copy public.product_product (id, name, description, price, available_on, updated_at, product_type_id, attributes, is_published, category_id, seo_description, seo_title, charge_taxes, tax_rate, weight) FROM '/tmp/p1.csv' CSV HEADER DELIMITER ',' FORCE NOT NULL attributes;


New!!!
copy public.product_product (id, name, description, price, publication_date, updated_at, product_type_id, attributes, is_published, category_id, seo_description, seo_title, charge_taxes, tax_rate, weight,description_json) FROM '/tmp/p8.csv' CSV HEADER DELIMITER ',' FORCE NOT NULL attributes;


product_productvariant:
copy public.product_productvariant (id, sku, name, price_override, product_id, attributes, cost_price, quantity, quantity_allocated, track_inventory, weight) FROM '/tmp/p2.csv' CSV HEADER FORCE NOT NULL name,attributes ;


product_productsimage:
copy public.product_productimage (id, image, ppoi, alt, sort_order, product_id) FROM '/tmp/p3.csv' CSV HEADER DELIMITER ',' FORCE NOT NULL alt;



Update Attribute
update public.product_product set attributes = attributes || '"1"=>"1"'::hstore where id > 182;

Update Brand

update public.product_product set attributes = attributes || '"3"=>"18"'::hstore where id > 348 and id <366;
select * from public.product_product where id = 348;
/dashboard/products/id/

Check Out Sequence:
/ds;

Check Next Sequence value:
Select nextval('product_product_id_seq');

Set Value Sequence:
Select setval('product_product_id_seq',294);

修改等级规格

##第一步
delete from tempmodify;
##第二步
copy public.tempmodify (id) FROM '/tmp/ar500.csv' CSV HEADER DELIMITER ',';
##第三步
update product_product
set attributes = attributes || '"1"=>"8","2"=>"10","3"=>"23"'::hstore
from tempmodify
where tempmodify.id = product_product.id;
