# products.py
import os

# Get absolute path to images directory
images_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "images"))

products = [
    {
        "name": "MacBook Pro 16\"",
        "price": 1499.99,
        "image": os.path.join(images_dir, "1.jpg"),
        "description": "Apple's flagship laptop with M2 Max chip",
        "category": "Laptops",
        "featured": True,
        "rating": 4.8,
        "reviews": [
            {
                "user": "TechEnthusiast123",
                "rating": 5,
                "comment": "Incredible performance and battery life!"
            },
            {
                "user": "DesignPro",
                "rating": 4.5,
                "comment": "Perfect for creative work, but a bit heavy"
            }
        ],
        "specs": {
            "processor": "Apple M2 Max",
            "memory": "32GB",
            "storage": "1TB SSD",
            "display": "16.2\" Liquid Retina XDR"
        },
        "features": [
            "Up to 22 hours battery life",
            "12-core CPU",
            "38-core GPU",
            "ProMotion technology"
        ],
        "in_stock": True,
        "discount": 0.1
    },
    {
        "name": "Dell XPS 15",
        "price": 1999.99,
        "image": os.path.join(images_dir, "2.jpg"),
        "description": "Powerful Windows laptop with OLED display",
        "category": "Laptops",
        "featured": True,
        "rating": 4.6,
        "reviews": [
            {
                "user": "WindowsFan",
                "rating": 4.7,
                "comment": "Best Windows laptop I've ever used"
            }
        ],
        "specs": {
            "processor": "Intel Core i7-12700H",
            "memory": "16GB",
            "storage": "512GB SSD",
            "display": "15.6\" OLED 3.5K"
        },
        "features": [
            "InfinityEdge display",
            "Carbon fiber palm rest",
            "Thunderbolt 4 ports",
            "Windows 11 Pro"
        ],
        "in_stock": True,
        "discount": 0.05
    },
    {
        "name": "iPhone 15 Pro",
        "price": 999.99,
        "image": os.path.join(images_dir, "3.jpg"),
        "description": "Apple's latest smartphone with A17 chip",
        "category": "Smartphones"
    },
    {
        "name": "Samsung Galaxy S23 Ultra",
        "price": 1199.99,
        "image": os.path.join(images_dir, "4.jpg"),
        "description": "Android flagship with 200MP camera",
        "category": "Smartphones"
    },
    {
        "name": "Sony WH-1000XM5",
        "price": 399.99,
        "image": os.path.join(images_dir, "5.jpg"),
        "description": "Noise-cancelling wireless headphones",
        "category": "Audio"
    },
    {
        "name": "Apple Watch Ultra",
        "price": 799.99,
        "image": os.path.join(images_dir, "6.jpg"),
        "description": "Rugged smartwatch for extreme sports",
        "category": "Wearables"
    },
    {
        "name": "Samsung 4K Smart TV",
        "price": 899.99,
        "image": os.path.join(images_dir, "7.jpg"),
        "description": "55\" 4K UHD Smart TV with HDR",
        "category": "TVs"
    },
    {
        "name": "Nintendo Switch OLED",
        "price": 349.99,
        "image": os.path.join(images_dir, "8.jpg"),
        "description": "Handheld gaming console with OLED screen",
        "category": "Gaming"
    },
    {
        "name": "PlayStation 5",
        "price": 499.99,
        "image": os.path.join(images_dir, "1.jpg"),
        "description": "Next-gen gaming console",
        "category": "Gaming"
    },
    {
        "name": "DJI Mavic 3 Pro",
        "price": 2199.99,
        "image": os.path.join(images_dir, "2.jpg"),
        "description": "Professional drone with 4/3 CMOS sensor",
        "category": "Drones"
    }
]
