import matplotlib.pyplot as plt
import matplotlib
import io, base64
from library.models import Searches
from .statistics_service import IStatisticsService

class MatplotlibStatisticsService(IStatisticsService):
    def get_search_counts(self, topics: list[str]) -> dict[str, int]:
        counts = {}
        for topic in topics:
            counts[topic] = Searches.objects.filter(choice=topic).count()
        return counts

    def generate_bar_chart(self, data: dict[str, int]) -> str:
        matplotlib.use('Agg')  # backend sin interfaz gráfica
        bar_positions = range(len(data))

        plt.bar(bar_positions, data.values(), color="#8B74DB")
        plt.xticks(bar_positions, data.keys(), rotation=45)
        plt.title("Searches per Topic")
        
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        buffer.seek(0)
        plt.close()

        graphic = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()
        return graphic
