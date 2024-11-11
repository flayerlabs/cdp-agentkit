from collections.abc import Callable

from cdp import Wallet
from pydantic import BaseModel, Field

from cdp_agentkit_core.actions import CdpAction
from cdp_agentkit_core.actions.wow.constants import (
    GENERIC_TOKEN_METADATA_URI,
    FLAUNCH_FACTORY_ABI,
    get_factory_address,
)

FLAUNCH_CREATE_TOKEN_PROMPT = """
This tool will create a Base FLAUNCH ERC20 memecoin using the WoW factory. This tool takes the token name and token symbol. It uses a bonding curve so there is no need to add liquidity to the pool upfront. It is only supported on Base Sepolia and (soon) Base Mainnet.
"""


class FlaunchCreateTokenInput(BaseModel):
    """Input argument schema for create token action."""

    name: str = Field(
        ...,
        description="The name of the token to create, e.g. FlaunchCoin",
    )
    symbol: str = Field(
        ...,
        description="The symbol of the token to create, e.g. FLAUNCH",
    )
    description: str = Field(
        ...,
        description="The description of the token to create, e.g. FlaunchCoin is a memecoin.",
    )


def flaunch_create_token(wallet: Wallet, name: str, symbol: str, description: str) -> str:
    """Create a Flaunch memecoin.

    Args:
        wallet (Wallet): The wallet to create the token from.
        name (str): The name of the token to create.
        symbol (str): The symbol of the token to create.
        description (str): The description of the token to create.

    Returns:
        str: A message containing the token creation details.

    """
    factory_address = get_factory_address(wallet.network_id)

    try:
        invocation = wallet.invoke_contract(
            contract_address=factory_address,
            method="deploy",
            abi=FLAUNCH_FACTORY_ABI,
            args={
                "_tokenCreator": wallet.default_address.address_id,
                "_platformReferrer": "0x0000000000000000000000000000000000000000",
                "_tokenURI": GENERIC_TOKEN_METADATA_URI,
                "_name": name,
                "_symbol": symbol,
                "_description": description,
            },
        ).wait()
    except Exception as e:
        return f"Error creating Flaunch memecoin {e!s}"

    return f"Created Flaunch memecoin {name} with symbol {symbol} on network {wallet.network_id}.\nTransaction hash for the token creation: {invocation.transaction.transaction_hash}\nTransaction link for the token creation: {invocation.transaction.transaction_link}"


class FlaunchCreateTokenAction(CdpAction):
    """Flaunch create token action."""

    name: str = "flaunch_create_token"
    description: str = FLAUNCH_CREATE_TOKEN_PROMPT
    args_schema: type[BaseModel] | None = FlaunchCreateTokenInput
    func: Callable[..., str] = flaunch_create_token