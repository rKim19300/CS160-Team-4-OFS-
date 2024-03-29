const router = require("express").Router();
const { DB } = require("../database");
const { checkLoggedIn, checkIsStaff } = require("../middleware/authMiddleware");

router.get("/allProducts", async (req, res) => {
    try {
        let allProducts = await DB.select_all_products();
        return res.status(200).json(allProducts);
    } catch (err) {
        console.log(`ERROR WHEN FETCHING ALL PRODUCTS: ${err}`);
        return res.status(400).send("Something went wrong when fetching store products");
    }
});

router.get("/productInfo/:prodID", checkLoggedIn, async (req, res) => {
    try {
        let product_id = req.params.prodID;
        let { productInfo, errMsg } = await DB.get_product_info(product_id);
        if (errMsg) return res.status(400).send(errMsg);
        return res.status(200).json(productInfo);
    } catch (err) {
        console.log(`ERROR WHEN GETTING PRODUCT INFO: ${err}`);
        return res.status(400).send("Something went wrong when getting product info");
    }
});

router.get("/allCategories", async (req, res) => {
    try {
        let all_categories = await DB.get_all_categories();
        return res.status(200).json(all_categories);
    } catch (err) {
        console.log(`ERROR WHEN FETCHING ALL CATEGORIES: ${err}`);
        return res.status(400).send("Something went wrong when fetching all product categories");
    }
});

router.post("/addCategory", checkIsStaff, async (req, res) => {
    try {
        let { category_name } = req.body;
        await DB.add_new_category(category_name);
        return res.status(200).send("Successfully added new category");
    } catch (err) {
        console.log(`ERROR WHEN ADDING A CATEGORY: ${err}`);
        return res.status(400).send("Something went wrong when fetching all product categories");
    }
});

router.post("/addProduct", checkIsStaff, async (req, res) => {
    try {
        let { name, description, image_url, price, weight, quantity, category_ids } = req.body;
        await DB.add_new_product(name, description, image_url, price, weight, quantity);
        await DB.set_product_categories(product_id, category_ids);
        return res.status(200).send("Successfully inserted product into database");
    } catch (err) {
        console.log(`ERROR WHEN ADDING PRODUCT: ${err}`);
        return res.status(400).send("Something went wrong when adding a product");
    }
});

router.post("/updateProduct/:prodID", checkIsStaff, async (req, res) => {
    try {
        let product_id = req.params.prodID;
        // Makes sure product_id actually exists
        let { errMsg } = await DB.get_product_info(product_id);
        if (errMsg) return res.status(400).send(errMsg);
        let { name, description, image_url, price, weight, quantity, category_ids } = req.body;
        await DB.update_product_info(product_id, name, description, image_url, price, weight, quantity);
        await DB.set_product_categories(product_id, category_ids);
        return res.status(200).send("Successfully updated product info");
    } catch (err) {
        console.log(`ERROR WHEN UPDATING PRODUCT: ${err}`);
        return res.status(400).send("Something went wrong when updating the product");
    }
});

module.exports = router;
