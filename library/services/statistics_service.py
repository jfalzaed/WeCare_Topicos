import abc

class IStatisticsService(abc.ABC):
    @abc.abstractmethod
    def get_search_counts(self, topics: list[str]) -> dict[str, int]:
        """Devuelve un diccionario con los conteos por tema"""
        pass

    @abc.abstractmethod
    def generate_bar_chart(self, data: dict[str, int]) -> str:
        """Devuelve la gráfica codificada en base64"""
        pass
