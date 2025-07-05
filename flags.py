from ldclient import LDClient
from ldclient.config import Config
from ldclient.context import Context
import os
from dotenv import load_dotenv

# Load the SDK key from the .env file
load_dotenv()
sdk_key = os.getenv("LD_SDK_KEY")

if not sdk_key:
    raise ValueError("❌ LD_SDK_KEY not found. Make sure your .env file exists.")

# Initialize LaunchDarkly client
ld_client = LDClient(Config(sdk_key))

if not ld_client.is_initialized():
    print("⚠️ LaunchDarkly SDK failed to initialize")
else:
    print("✅ LaunchDarkly SDK initialized successfully")

# Function to evaluate a feature flag for a given user context
def check_flag(flag_key: str, user_key="user-key-123", name="Jorge", plan="premium"):
    context = Context.builder(user_key) \
        .kind("user") \
        .name(name) \
        .set("plan", plan) \
        .build()

    result = ld_client.variation(flag_key, context, False)
    print(f"[LaunchDarkly] Flag '{flag_key}' evaluated as {result} for user '{user_key}' with plan='{plan}'")
    return result

# Make ld_client accessible from app.py
__all__ = ["check_flag", "ld_client"]

