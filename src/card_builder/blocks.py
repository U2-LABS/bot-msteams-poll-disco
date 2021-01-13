MAIN_BLOCK = {
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.0",
    "body": [
        # Rows with songs
    ]
}

SONG_ROW = {
    "type": "ColumnSet",
    "columns": [
      {
          "type": "Column",
          "width": "320px",
          "items": [
              {
                  "type": "TextBlock",
                  "text": "Song details",
                  "wrap": True,
                  "height": "stretch",
                  "spacing": "None"
              }
          ],
          "height": "stretch",
          "spacing": "None",
          "verticalContentAlignment": "Center",
          "minHeight": "0px"
      },
      {
          "type": "Column",
          "width": "stretch",
          "items": [
              {
                  "type": "ActionSet",
                  "actions": [
                      {
                          "type": "Action.Submit",
                          "title": "Vote",
                          "style": "positive",
                          "data": {
                              "song_id": 1
                          }
                      }
                  ]
              }
          ]
      }
    ]
}
