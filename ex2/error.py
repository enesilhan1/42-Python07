class InvalidStrategyError(Exception):
    def __init__(self, name: str, strategy: str) -> None:
        super().__init__(
            f"Invalid Creature '{name} '"
            f"for this {strategy} strategy"
            )
