from app.models.statistics import StatisticsResponse

# Datos simulados / Mock data
async def get_general_statistics() -> StatisticsResponse:
    return StatisticsResponse(
        total_users=123,
        total_boards=47,
        pending_tasks=320,
        completed_tasks=278
    )