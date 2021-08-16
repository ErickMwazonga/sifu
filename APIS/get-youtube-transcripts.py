from youtube_transcript_api import YouTubeTranscriptApi


def generate_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        script = ""

        for text in transcript:
            t = text["text"]
            if t != '[Music]':
                script += t + " "

        print(script)

    except Exception as e:
        print('Subtitles are disabled for this video')
        return


generate_transcript("AyRHwsbJa1s")
