from ldclient import LDClient
from ldclient.config import Config
from ldclient.context import Context
import os
from dotenv import load_dotenv

load_dotenv()
sdk_key = os.getenv("LD_SDK_KEY")
ld_client = LDClient(Config(sdk_key))

context = Context.builder("temp-user-456") \
    .kind("user") \
    .name("TestUser") \
    .set("plan", "premium") \
    .build()

# Trigger an evaluation
flag_value = ld_client.variation("jcr-ui-feature", context, False)
print("Triggered evaluation with context. Flag value:", flag_value)

ld_client.close()

