from flask import Flask, render_template, jsonify, request
from flags import check_flag, ld_client
from ldclient.context import Context

app = Flask(__name__)

@app.route("/")
def index():
    show_feature = check_flag("jcr-ui-feature")
    print(f"🌐 [/] Rendering index with show_feature = {show_feature}")
    return render_template("index.html", show_feature=show_feature)

@app.route("/api/feature")
def api_feature():
    print("✅ /api/feature endpoint was hit")
    try:
        show_feature = check_flag("jcr-ui-feature")
        print(f"🔧 LaunchDarkly flag evaluated to: {show_feature}")
        return jsonify({"showFeature": show_feature})
    except Exception as e:
        print(f"❌ Error in /api/feature: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/api/cta-click", methods=["POST"])
def track_cta_click():
    try:
        data = request.get_json()
        user_key = data.get("user_key", "user-key-123")

        # ✅ Properly build a LaunchDarkly context object
        context = Context.builder(user_key) \
            .kind("user") \
            .name("Jorge") \
            .set("plan", "premium") \
            .build()

        ld_client.track("cta-click", context)
        print(f"📈 Tracked CTA click for user: {user_key}")
        return jsonify({"status": "CTA click tracked"})
    except Exception as e:
        print(f"❌ Error tracking CTA click: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("🚀 Starting Flask app on port 5050...")
    app.run(debug=True, host="127.0.0.1", port=5050)

