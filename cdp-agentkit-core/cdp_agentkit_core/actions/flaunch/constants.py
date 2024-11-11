FLAUNCH_FACTORY_ABI = [
  {
    "type": "constructor",
    "inputs": [
      {
        "name": "params",
        "type": "tuple",
        "internalType": "struct PositionManager.ConstructorParams",
        "components": [
          {
            "name": "nativeToken",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "poolManager",
            "type": "address",
            "internalType": "contract IPoolManager"
          },
          {
            "name": "feeDistribution",
            "type": "tuple",
            "internalType": "struct FeeDistributor.FeeDistribution",
            "components": [
              {
                "name": "swapFee",
                "type": "uint24",
                "internalType": "uint24"
              },
              {
                "name": "referrer",
                "type": "uint24",
                "internalType": "uint24"
              },
              {
                "name": "protocol",
                "type": "uint24",
                "internalType": "uint24"
              },
              {
                "name": "active",
                "type": "bool",
                "internalType": "bool"
              }
            ]
          },
          {
            "name": "initialPrice",
            "type": "address",
            "internalType": "contract IInitialPrice"
          },
          {
            "name": "protocolOwner",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "protocolFeeRecipient",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "flayGovernance",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "feeExemptions",
            "type": "address",
            "internalType": "contract FeeExemptions"
          }
        ]
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "receive",
    "stateMutability": "payable"
  },
  {
    "type": "function",
    "name": "MAX_CREATOR_ALLOCATION",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "uint24",
        "internalType": "uint24"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "MAX_PROTOCOL_ALLOCATION",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "uint24",
        "internalType": "uint24"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "actionManager",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "contract TreasuryActionManager"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "afterAddLiquidity",
    "inputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "_key",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct IPoolManager.ModifyLiquidityParams",
        "components": [
          {
            "name": "tickLower",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "tickUpper",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "liquidityDelta",
            "type": "int256",
            "internalType": "int256"
          },
          {
            "name": "salt",
            "type": "bytes32",
            "internalType": "bytes32"
          }
        ]
      },
      {
        "name": "",
        "type": "int256",
        "internalType": "BalanceDelta"
      },
      {
        "name": "",
        "type": "int256",
        "internalType": "BalanceDelta"
      },
      {
        "name": "",
        "type": "bytes",
        "internalType": "bytes"
      }
    ],
    "outputs": [
      {
        "name": "selector_",
        "type": "bytes4",
        "internalType": "bytes4"
      },
      {
        "name": "",
        "type": "int256",
        "internalType": "BalanceDelta"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "afterDonate",
    "inputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "_key",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      },
      {
        "name": "",
        "type": "uint256",
        "internalType": "uint256"
      },
      {
        "name": "",
        "type": "uint256",
        "internalType": "uint256"
      },
      {
        "name": "",
        "type": "bytes",
        "internalType": "bytes"
      }
    ],
    "outputs": [
      {
        "name": "selector_",
        "type": "bytes4",
        "internalType": "bytes4"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "afterInitialize",
    "inputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "_key",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      },
      {
        "name": "",
        "type": "uint160",
        "internalType": "uint160"
      },
      {
        "name": "",
        "type": "int24",
        "internalType": "int24"
      }
    ],
    "outputs": [
      {
        "name": "selector_",
        "type": "bytes4",
        "internalType": "bytes4"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "afterRemoveLiquidity",
    "inputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "_key",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct IPoolManager.ModifyLiquidityParams",
        "components": [
          {
            "name": "tickLower",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "tickUpper",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "liquidityDelta",
            "type": "int256",
            "internalType": "int256"
          },
          {
            "name": "salt",
            "type": "bytes32",
            "internalType": "bytes32"
          }
        ]
      },
      {
        "name": "",
        "type": "int256",
        "internalType": "BalanceDelta"
      },
      {
        "name": "",
        "type": "int256",
        "internalType": "BalanceDelta"
      },
      {
        "name": "",
        "type": "bytes",
        "internalType": "bytes"
      }
    ],
    "outputs": [
      {
        "name": "selector_",
        "type": "bytes4",
        "internalType": "bytes4"
      },
      {
        "name": "",
        "type": "int256",
        "internalType": "BalanceDelta"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "afterSwap",
    "inputs": [
      {
        "name": "_sender",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "_key",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      },
      {
        "name": "_params",
        "type": "tuple",
        "internalType": "struct IPoolManager.SwapParams",
        "components": [
          {
            "name": "zeroForOne",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "amountSpecified",
            "type": "int256",
            "internalType": "int256"
          },
          {
            "name": "sqrtPriceLimitX96",
            "type": "uint160",
            "internalType": "uint160"
          }
        ]
      },
      {
        "name": "_delta",
        "type": "int256",
        "internalType": "BalanceDelta"
      },
      {
        "name": "_hookData",
        "type": "bytes",
        "internalType": "bytes"
      }
    ],
    "outputs": [
      {
        "name": "selector_",
        "type": "bytes4",
        "internalType": "bytes4"
      },
      {
        "name": "hookDeltaUnspecified_",
        "type": "int128",
        "internalType": "int128"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "balances",
    "inputs": [
      {
        "name": "_recipient",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [
      {
        "name": "_amount",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "beforeAddLiquidity",
    "inputs": [
      {
        "name": "_sender",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "_key",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct IPoolManager.ModifyLiquidityParams",
        "components": [
          {
            "name": "tickLower",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "tickUpper",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "liquidityDelta",
            "type": "int256",
            "internalType": "int256"
          },
          {
            "name": "salt",
            "type": "bytes32",
            "internalType": "bytes32"
          }
        ]
      },
      {
        "name": "",
        "type": "bytes",
        "internalType": "bytes"
      }
    ],
    "outputs": [
      {
        "name": "selector_",
        "type": "bytes4",
        "internalType": "bytes4"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "beforeDonate",
    "inputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      },
      {
        "name": "",
        "type": "uint256",
        "internalType": "uint256"
      },
      {
        "name": "",
        "type": "uint256",
        "internalType": "uint256"
      },
      {
        "name": "",
        "type": "bytes",
        "internalType": "bytes"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "bytes4",
        "internalType": "bytes4"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "beforeInitialize",
    "inputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      },
      {
        "name": "",
        "type": "uint160",
        "internalType": "uint160"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "bytes4",
        "internalType": "bytes4"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "beforeRemoveLiquidity",
    "inputs": [
      {
        "name": "_sender",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "_key",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct IPoolManager.ModifyLiquidityParams",
        "components": [
          {
            "name": "tickLower",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "tickUpper",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "liquidityDelta",
            "type": "int256",
            "internalType": "int256"
          },
          {
            "name": "salt",
            "type": "bytes32",
            "internalType": "bytes32"
          }
        ]
      },
      {
        "name": "",
        "type": "bytes",
        "internalType": "bytes"
      }
    ],
    "outputs": [
      {
        "name": "selector_",
        "type": "bytes4",
        "internalType": "bytes4"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "beforeSwap",
    "inputs": [
      {
        "name": "_sender",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "_key",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      },
      {
        "name": "_params",
        "type": "tuple",
        "internalType": "struct IPoolManager.SwapParams",
        "components": [
          {
            "name": "zeroForOne",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "amountSpecified",
            "type": "int256",
            "internalType": "int256"
          },
          {
            "name": "sqrtPriceLimitX96",
            "type": "uint160",
            "internalType": "uint160"
          }
        ]
      },
      {
        "name": "_hookData",
        "type": "bytes",
        "internalType": "bytes"
      }
    ],
    "outputs": [
      {
        "name": "selector_",
        "type": "bytes4",
        "internalType": "bytes4"
      },
      {
        "name": "beforeSwapDelta_",
        "type": "int256",
        "internalType": "BeforeSwapDelta"
      },
      {
        "name": "",
        "type": "uint24",
        "internalType": "uint24"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "bidWall",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "contract BidWallThreshold"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "cancelOwnershipHandover",
    "inputs": [],
    "outputs": [],
    "stateMutability": "payable"
  },
  {
    "type": "function",
    "name": "closeBidWall",
    "inputs": [
      {
        "name": "_key",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      }
    ],
    "outputs": [],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "completeOwnershipHandover",
    "inputs": [
      {
        "name": "pendingOwner",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [],
    "stateMutability": "payable"
  },
  {
    "type": "function",
    "name": "fairLaunch",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "contract FairLaunch"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "feeCalculator",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "contract IFeeCalculator"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "feeExemptions",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "contract FeeExemptions"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "feeSplit",
    "inputs": [
      {
        "name": "_poolId",
        "type": "bytes32",
        "internalType": "PoolId"
      },
      {
        "name": "_amount",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "outputs": [
      {
        "name": "bidWall_",
        "type": "uint256",
        "internalType": "uint256"
      },
      {
        "name": "creator_",
        "type": "uint256",
        "internalType": "uint256"
      },
      {
        "name": "protocol_",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "flaunch",
    "inputs": [
      {
        "name": "_name",
        "type": "string",
        "internalType": "string"
      },
      {
        "name": "_symbol",
        "type": "string",
        "internalType": "string"
      },
      {
        "name": "_tokenUri",
        "type": "string",
        "internalType": "string"
      },
      {
        "name": "_initialTokenFairLaunch",
        "type": "uint256",
        "internalType": "uint256"
      },
      {
        "name": "_creatorFeeAllocation",
        "type": "uint24",
        "internalType": "uint24"
      },
      {
        "name": "_vitaminAllocation",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "outputs": [
      {
        "name": "memecoin_",
        "type": "address",
        "internalType": "address"
      }
    ],
    "stateMutability": "payable"
  },
  {
    "type": "function",
    "name": "flayGovernance",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "address"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getHookPermissions",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct Hooks.Permissions",
        "components": [
          {
            "name": "beforeInitialize",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "afterInitialize",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "beforeAddLiquidity",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "afterAddLiquidity",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "beforeRemoveLiquidity",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "afterRemoveLiquidity",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "beforeSwap",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "afterSwap",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "beforeDonate",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "afterDonate",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "beforeSwapReturnDelta",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "afterSwapReturnDelta",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "afterAddLiquidityReturnDelta",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "afterRemoveLiquidityReturnDelta",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "stateMutability": "pure"
  },
  {
    "type": "function",
    "name": "getPoolFeeDistribution",
    "inputs": [
      {
        "name": "_poolId",
        "type": "bytes32",
        "internalType": "PoolId"
      }
    ],
    "outputs": [
      {
        "name": "feeDistribution_",
        "type": "tuple",
        "internalType": "struct FeeDistributor.FeeDistribution",
        "components": [
          {
            "name": "swapFee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "referrer",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "protocol",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "active",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "nativeToken",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "address"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "owner",
    "inputs": [],
    "outputs": [
      {
        "name": "result",
        "type": "address",
        "internalType": "address"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "ownershipHandoverExpiresAt",
    "inputs": [
      {
        "name": "pendingOwner",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [
      {
        "name": "result",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "poolFees",
    "inputs": [
      {
        "name": "_poolKey",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct InternalSwapPool.ClaimableFees",
        "components": [
          {
            "name": "amount0",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "amount1",
            "type": "uint256",
            "internalType": "uint256"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "poolKey",
    "inputs": [
      {
        "name": "_token",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "poolManager",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "contract IPoolManager"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "protocolFeeRecipient",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "address"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "renounceOwnership",
    "inputs": [],
    "outputs": [],
    "stateMutability": "payable"
  },
  {
    "type": "function",
    "name": "requestOwnershipHandover",
    "inputs": [],
    "outputs": [],
    "stateMutability": "payable"
  },
  {
    "type": "function",
    "name": "setCreatorFeeAllocation",
    "inputs": [
      {
        "name": "_key",
        "type": "tuple",
        "internalType": "struct PoolKey",
        "components": [
          {
            "name": "currency0",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "currency1",
            "type": "address",
            "internalType": "Currency"
          },
          {
            "name": "fee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "tickSpacing",
            "type": "int24",
            "internalType": "int24"
          },
          {
            "name": "hooks",
            "type": "address",
            "internalType": "contract IHooks"
          }
        ]
      },
      {
        "name": "_allocation",
        "type": "uint24",
        "internalType": "uint24"
      }
    ],
    "outputs": [],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "setFeeCalculator",
    "inputs": [
      {
        "name": "_feeCalculator",
        "type": "address",
        "internalType": "contract IFeeCalculator"
      }
    ],
    "outputs": [],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "setFeeDistribution",
    "inputs": [
      {
        "name": "_feeDistribution",
        "type": "tuple",
        "internalType": "struct FeeDistributor.FeeDistribution",
        "components": [
          {
            "name": "swapFee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "referrer",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "protocol",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "active",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "outputs": [],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "setFlaunch",
    "inputs": [
      {
        "name": "_flaunchContract",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "setInitialPrice",
    "inputs": [
      {
        "name": "_initialPrice",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "setPoolFeeDistribution",
    "inputs": [
      {
        "name": "_poolId",
        "type": "bytes32",
        "internalType": "PoolId"
      },
      {
        "name": "_feeDistribution",
        "type": "tuple",
        "internalType": "struct FeeDistributor.FeeDistribution",
        "components": [
          {
            "name": "swapFee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "referrer",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "protocol",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "active",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "outputs": [],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "setProtocolFeeDistribution",
    "inputs": [
      {
        "name": "_protocol",
        "type": "uint24",
        "internalType": "uint24"
      }
    ],
    "outputs": [],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "transferOwnership",
    "inputs": [
      {
        "name": "newOwner",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [],
    "stateMutability": "payable"
  },
  {
    "type": "function",
    "name": "unlockCallback",
    "inputs": [
      {
        "name": "data",
        "type": "bytes",
        "internalType": "bytes"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "bytes",
        "internalType": "bytes"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "withdrawFees",
    "inputs": [
      {
        "name": "_recipient",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "_unwrap",
        "type": "bool",
        "internalType": "bool"
      }
    ],
    "outputs": [],
    "stateMutability": "nonpayable"
  },
  {
    "type": "event",
    "name": "CreatorFeeAllocationUpdated",
    "inputs": [
      {
        "name": "_poolId",
        "type": "bytes32",
        "indexed": true,
        "internalType": "PoolId"
      },
      {
        "name": "_allocation",
        "type": "uint24",
        "indexed": false,
        "internalType": "uint24"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "Deposit",
    "inputs": [
      {
        "name": "_poolId",
        "type": "bytes32",
        "indexed": true,
        "internalType": "PoolId"
      },
      {
        "name": "_payee",
        "type": "address",
        "indexed": false,
        "internalType": "address"
      },
      {
        "name": "_token",
        "type": "address",
        "indexed": false,
        "internalType": "address"
      },
      {
        "name": "_amount",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "FeeCalculatorUpdated",
    "inputs": [
      {
        "name": "_feeCalculator",
        "type": "address",
        "indexed": false,
        "internalType": "address"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "FeeDistributionUpdated",
    "inputs": [
      {
        "name": "_feeDistribution",
        "type": "tuple",
        "indexed": false,
        "internalType": "struct FeeDistributor.FeeDistribution",
        "components": [
          {
            "name": "swapFee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "referrer",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "protocol",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "active",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "InitialPriceUpdated",
    "inputs": [
      {
        "name": "_initialPrice",
        "type": "address",
        "indexed": false,
        "internalType": "address"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "OwnershipHandoverCanceled",
    "inputs": [
      {
        "name": "pendingOwner",
        "type": "address",
        "indexed": true,
        "internalType": "address"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "OwnershipHandoverRequested",
    "inputs": [
      {
        "name": "pendingOwner",
        "type": "address",
        "indexed": true,
        "internalType": "address"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "OwnershipTransferred",
    "inputs": [
      {
        "name": "oldOwner",
        "type": "address",
        "indexed": true,
        "internalType": "address"
      },
      {
        "name": "newOwner",
        "type": "address",
        "indexed": true,
        "internalType": "address"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "PoolCreated",
    "inputs": [
      {
        "name": "_poolId",
        "type": "bytes32",
        "indexed": true,
        "internalType": "PoolId"
      },
      {
        "name": "_initialTokenFairLaunch",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      },
      {
        "name": "_fairLaunchEnds",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      },
      {
        "name": "_memecoin",
        "type": "address",
        "indexed": false,
        "internalType": "address"
      },
      {
        "name": "_memecoinTreasury",
        "type": "address",
        "indexed": false,
        "internalType": "address"
      },
      {
        "name": "_tokenId",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      },
      {
        "name": "_currencyFlipped",
        "type": "bool",
        "indexed": false,
        "internalType": "bool"
      },
      {
        "name": "_flaunchFee",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      },
      {
        "name": "_creator",
        "type": "address",
        "indexed": false,
        "internalType": "address"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "PoolFeeDistributionUpdated",
    "inputs": [
      {
        "name": "_poolId",
        "type": "bytes32",
        "indexed": true,
        "internalType": "PoolId"
      },
      {
        "name": "_feeDistribution",
        "type": "tuple",
        "indexed": false,
        "internalType": "struct FeeDistributor.FeeDistribution",
        "components": [
          {
            "name": "swapFee",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "referrer",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "protocol",
            "type": "uint24",
            "internalType": "uint24"
          },
          {
            "name": "active",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "PoolFeesDistributed",
    "inputs": [
      {
        "name": "_poolId",
        "type": "bytes32",
        "indexed": true,
        "internalType": "PoolId"
      },
      {
        "name": "_donateAmount",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      },
      {
        "name": "_creatorAmount",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      },
      {
        "name": "_bidWallAmount",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      },
      {
        "name": "_governanceAmount",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      },
      {
        "name": "_protocolAmount",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "PoolFeesReceived",
    "inputs": [
      {
        "name": "_poolId",
        "type": "bytes32",
        "indexed": true,
        "internalType": "PoolId"
      },
      {
        "name": "_amount0",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      },
      {
        "name": "_amount1",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "PoolFeesSwapped",
    "inputs": [
      {
        "name": "_poolId",
        "type": "bytes32",
        "indexed": true,
        "internalType": "PoolId"
      },
      {
        "name": "zeroForOne",
        "type": "bool",
        "indexed": false,
        "internalType": "bool"
      },
      {
        "name": "_amount0",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      },
      {
        "name": "_amount1",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "PoolStateUpdated",
    "inputs": [
      {
        "name": "_poolId",
        "type": "bytes32",
        "indexed": true,
        "internalType": "PoolId"
      },
      {
        "name": "_sqrtPriceX96",
        "type": "uint160",
        "indexed": false,
        "internalType": "uint160"
      },
      {
        "name": "_tick",
        "type": "int24",
        "indexed": false,
        "internalType": "int24"
      },
      {
        "name": "_protocolFee",
        "type": "uint24",
        "indexed": false,
        "internalType": "uint24"
      },
      {
        "name": "_swapFee",
        "type": "uint24",
        "indexed": false,
        "internalType": "uint24"
      },
      {
        "name": "_liquidity",
        "type": "uint128",
        "indexed": false,
        "internalType": "uint128"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "PoolSwap",
    "inputs": [
      {
        "name": "poolId",
        "type": "bytes32",
        "indexed": true,
        "internalType": "PoolId"
      },
      {
        "name": "flAmount0",
        "type": "int256",
        "indexed": false,
        "internalType": "int256"
      },
      {
        "name": "flAmount1",
        "type": "int256",
        "indexed": false,
        "internalType": "int256"
      },
      {
        "name": "flFee0",
        "type": "int256",
        "indexed": false,
        "internalType": "int256"
      },
      {
        "name": "flFee1",
        "type": "int256",
        "indexed": false,
        "internalType": "int256"
      },
      {
        "name": "ispAmount0",
        "type": "int256",
        "indexed": false,
        "internalType": "int256"
      },
      {
        "name": "ispAmount1",
        "type": "int256",
        "indexed": false,
        "internalType": "int256"
      },
      {
        "name": "ispFee0",
        "type": "int256",
        "indexed": false,
        "internalType": "int256"
      },
      {
        "name": "ispFee1",
        "type": "int256",
        "indexed": false,
        "internalType": "int256"
      },
      {
        "name": "uniAmount0",
        "type": "int256",
        "indexed": false,
        "internalType": "int256"
      },
      {
        "name": "uniAmount1",
        "type": "int256",
        "indexed": false,
        "internalType": "int256"
      },
      {
        "name": "uniFee0",
        "type": "int256",
        "indexed": false,
        "internalType": "int256"
      },
      {
        "name": "uniFee1",
        "type": "int256",
        "indexed": false,
        "internalType": "int256"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "ReferrerFeePaid",
    "inputs": [
      {
        "name": "_poolId",
        "type": "bytes32",
        "indexed": true,
        "internalType": "PoolId"
      },
      {
        "name": "_recipient",
        "type": "address",
        "indexed": false,
        "internalType": "address"
      },
      {
        "name": "_token",
        "type": "address",
        "indexed": false,
        "internalType": "address"
      },
      {
        "name": "_amount",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      }
    ],
    "anonymous": false
  },
  {
    "type": "event",
    "name": "Withdrawal",
    "inputs": [
      {
        "name": "_sender",
        "type": "address",
        "indexed": false,
        "internalType": "address"
      },
      {
        "name": "_recipient",
        "type": "address",
        "indexed": false,
        "internalType": "address"
      },
      {
        "name": "_token",
        "type": "address",
        "indexed": false,
        "internalType": "address"
      },
      {
        "name": "_amount",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      }
    ],
    "anonymous": false
  },
  {
    "type": "error",
    "name": "AlreadyInitialized",
    "inputs": []
  },
  {
    "type": "error",
    "name": "CallerIsNotBidWall",
    "inputs": []
  },
  {
    "type": "error",
    "name": "CallerNotCreator",
    "inputs": [
      {
        "name": "_caller",
        "type": "address",
        "internalType": "address"
      }
    ]
  },
  {
    "type": "error",
    "name": "CannotBeInitializedDirectly",
    "inputs": []
  },
  {
    "type": "error",
    "name": "CannotModifyLiquidityDuringFairLaunch",
    "inputs": []
  },
  {
    "type": "error",
    "name": "CannotSellTokenDuringFairLaunch",
    "inputs": []
  },
  {
    "type": "error",
    "name": "CreatorFeeAllocationInvalid",
    "inputs": [
      {
        "name": "_allocation",
        "type": "uint24",
        "internalType": "uint24"
      },
      {
        "name": "_maxAllocation",
        "type": "uint256",
        "internalType": "uint256"
      }
    ]
  },
  {
    "type": "error",
    "name": "HookNotImplemented",
    "inputs": []
  },
  {
    "type": "error",
    "name": "InsufficientFlaunchFee",
    "inputs": [
      {
        "name": "_paid",
        "type": "uint256",
        "internalType": "uint256"
      },
      {
        "name": "_required",
        "type": "uint256",
        "internalType": "uint256"
      }
    ]
  },
  {
    "type": "error",
    "name": "InvalidPool",
    "inputs": []
  },
  {
    "type": "error",
    "name": "LockFailure",
    "inputs": []
  },
  {
    "type": "error",
    "name": "NewOwnerIsZeroAddress",
    "inputs": []
  },
  {
    "type": "error",
    "name": "NoHandoverRequest",
    "inputs": []
  },
  {
    "type": "error",
    "name": "NotPoolManager",
    "inputs": []
  },
  {
    "type": "error",
    "name": "NotSelf",
    "inputs": []
  },
  {
    "type": "error",
    "name": "ProtocolFeeInvalid",
    "inputs": []
  },
  {
    "type": "error",
    "name": "RecipientZeroAddress",
    "inputs": []
  },
  {
    "type": "error",
    "name": "ReferrerFeeInvalid",
    "inputs": []
  },
  {
    "type": "error",
    "name": "SwapFeeInvalid",
    "inputs": []
  },
  {
    "type": "error",
    "name": "TooManyVitamins",
    "inputs": []
  },
  {
    "type": "error",
    "name": "Unauthorized",
    "inputs": []
  }
]

FLAUNCH_FACTORY_CONTRACT_ADDRESSES = {
    "base-sepolia": "0xE982F970859383cF3A4221184330aa7B1AAE7fdc",
    "base-mainnet": "0x0",
}


def get_factory_address(network: str) -> str:
    """Get the Base Flaunch ERC20 Factory contract address for the specified network.

    Args:
        network (str): The network ID to get the contract address for.
            Valid networks are: base-sepolia, base-mainnet.

    Returns:
        str: The contract address for the specified network.

    Raises:
        ValueError: If the specified network is not supported.

    """
    network = network.lower()
    if network not in FLAUNCH_FACTORY_CONTRACT_ADDRESSES:
        raise ValueError(
            f"Invalid network: {network}. Valid networks are: {', '.join(FLAUNCH_FACTORY_CONTRACT_ADDRESSES.keys())}"
        )
    return FLAUNCH_FACTORY_CONTRACT_ADDRESSES[network]


GENERIC_TOKEN_METADATA_URI = "ipfs://QmfXzbWQY1wBzq3k9mCthN9prVAYpJGfZ4ekcxMiAq5Xhg"
