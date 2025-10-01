from .statistics_service import IStatisticsService

class FakeStatisticsService(IStatisticsService):
    def get_search_counts(self, topics: list[str]) -> dict[str, int]:
        # Devuelve datos fijos para pruebas
        return {topic: 10 for topic in topics}

    def generate_bar_chart(self, data: dict[str, int]) -> str:
        # Simula devolver una gráfica falsa
        return "fake_base64_image"
