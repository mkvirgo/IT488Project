from flask import Blueprint
import views

main = Blueprint("main", __name__)

main.add_url_rule("/", view_func=views.home, methods=["GET"])

main.add_url_rule("/api/health", view_func=views.health, methods=["GET", "OPTIONS"])

main.add_url_rule("/api/items", view_func=views.list_items, methods=["GET", "OPTIONS"])
main.add_url_rule("/api/items", view_func=views.create_item, methods=["POST", "OPTIONS"])

main.add_url_rule("/api/items/<int:item_id>", view_func=views.get_item, methods=["GET", "OPTIONS"])
main.add_url_rule("/api/items/<int:item_id>", view_func=views.update_item, methods=["PUT", "OPTIONS"])
main.add_url_rule("/api/items/<int:item_id>", view_func=views.delete_item, methods=["DELETE", "OPTIONS"])
