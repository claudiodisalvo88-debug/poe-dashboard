from app.schemas.node import NodeEnergyData


class NodeDataService:
    def __init__(self) -> None:
        self._items: list[dict] = []

    def save_node_data(self, payload: NodeEnergyData) -> dict:
        item = payload.model_dump()
        self._items.append(item)
        return item

    def get_all_node_data(self) -> list[dict]:
        return self._items


node_data_service = NodeDataService()