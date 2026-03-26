#!/usr/bin/env bash

FOLDER=$1
NAME=$2

if [ -z "$FOLDER" ] || [ -z "$NAME" ]; then
  echo "Usage: bash generate.sh <folder> <ComponentName>"
  exit 1
fi

BASE_DIR="./src/$FOLDER/$NAME"

mkdir -p "$BASE_DIR"

SCSS_FILE="$BASE_DIR/$NAME.scss"
JS_FILE="$BASE_DIR/$NAME.js"

# Generate SCSS module
cat <<EOF > "$SCSS_FILE"
.$NAME {
  outline: 2px dotted red;
}
EOF

# Generate Mithril component
cat <<EOF > "$JS_FILE"
import m from "mithril"
import "./$NAME.scss"

export default {
  view() {
    return m("div.$NAME",  [
      "Hello, from $NAME!"
    ])
  }
}
EOF

echo "✔ Generated $NAME in src/$FOLDER/$NAME"