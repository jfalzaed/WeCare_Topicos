from .matplotlib_statistics_service import MatplotlibStatisticsService
from .statistics_service import IStatisticsService

def create_statistics_service(provider="matplotlib") -> IStatisticsService:
    if provider == "matplotlib":
        return MatplotlibStatisticsService()
    # aquí podrías agregar más proveedores (ej: SeabornService, PlotlyService)
    return MatplotlibStatisticsService()
