from gettext import gettext as _
SKILL_NAME = "私のサンタクロース"

LAUNCH_NOT_PERSONALIZE = _(
    "すみません。誰の声か識別できませんでした。このスキルでは音声プロフィールの登録が必要です。" \
    + "もし音声プロフィールの登録がまだの場合はアレクサアプリにで音声プロフィールを登録してください。" \
    + "すでに有効にされている場合は、聞き取れなかった可能性がありますので再度お試しください。" \
    + "スキルの詳細を知りたい場合は、「アレクサ、{}を開いて、ヘルプ」といってください".format(SKILL_NAME))
LAUNCH_NO_SANTA = _(
    "{} は最初にサンタとしての登録が必要です。サンタとして登録したユーザーが、サンタへの願い事を聞くスキルです。".format(SKILL_NAME) \
    + "まずはあなたがサンタとして登録するのかどうかを教えてください。「サンタです」、もしくは、「違う人です」と答えてください" )
LAUNCH_NO_SANTA_REPROMPT = _(
    "まずはあなたがサンタとして登録するのかどうかを教えてください。「サンタです」、もしくは、「違う人です」と答えてください" )
LAUNCH_IS_PARENT = _(
    "こんにちは、<alexa:name type='first' personId='{}'/>さん。「願い事を確認」というと願い事を聞けます。" \
    + "使い方を知りたい場合は「ヘルプ」といってください。")
LAUNCH_IS_CHILD = _(
    "こんにちは。このスキルではサンタへの願い事を登録できます。" \
    + "「願い事をする」と言ってくださいね。" \
    + "")
ANSWER_CLASS_NOT_PERSONALIZE = _(
    "すみません。誰の声か識別できませんでした。このスキルでは音声プロフィールの登録が必要です。" \
    + "「サンタです」、もしくは「違う人です」ともう一度、ゆっくりと言ってみてください。" )
ANSWER_CLASS_IS_PARENT = _(
    "承知しました、<alexa:name type='first' personId='{}'/>さん。それでは「サンタ」として登録しますね。" \
    + "<alexa:name type='first' personId='{}'/>さんは、みんなの「願いごと」を確認する事ができます。" \
    + "まずは、みんなに{}で遊んでもらって願い事を登録してもらってくださいね。".format(SKILL_NAME) \
    + "願い事が登録されると「願い事を聞く」と言ってみてください。ではまた。")
ANSWER_CLASS_IS_CHILD = _(
    "こんにちは。このスキルではサンタへの願い事を登録できます。" \
    + "「願い事をする」と言ってくださいね。" \
    + "")
ANSWER_CLASS_IS_NG = _(
    "すみません。{} は最初にサンタとしての登録が必要です。サンタとして登録したユーザーが、サンタへの願い事を聞くスキルです。".format(SKILL_NAME) \
    + "まずはスキルにサンタを登録してください" )
PREMIUM_INFO_MSG = _(
    "こんにちは")
ADD_NO_MSG = _(
    "登録を取りやめました。登録をやり直す場合には「願い事をする」と言ってください。")
BUY_MSG = _(
    "こんにちは")
BUY_COMPLETE_MSG = _(
    "こんにちは")
BUY_CANCEL_MSG = _(
    "こんにちは")
CANCEL_SUBSCRIPTION_MSG = _(
    "こんにちは")
WELCOME_MESSAGE = _(
    "こんにちは")
WISH_ADD_CONFIRM_MSG = _(
    "わかりました、<alexa:name type='first' personId='{}'/>さん。" \
     + "{}、ですね。よろしければ「はい」といってください。")
WISH_ADD_CONFIRM_NONAME_MSG = _(
    "{}、ですね。よろしければ「はい」といってください。")
WISH_ADD_MSG = _(
    "わかりました、<alexa:name type='first' personId='{}'/>さん。" \
    + "{}、ですね。願い事を登録しました。使ってくれてありがとう。ではまた。")
WISH_ADD_NONAME_MSG = _(
    "{}、ですね。願い事を登録しました。使ってくれてありがとう。ではまた。")
WISH_ADD_PARENT_MSG = _("{}、ですね。おや？自分への願い事ですか？登録した願い事を確認するときは「願い事を確認」と言ってくださいね。")
WISH_ADD_TIMEOUT_MSG = _("すみません。お返事がタイムアウトしてしまいました。もう一度「願い事をする」からお願いします。")
WISH_ADD_NO_MSG = _("願い事の登録を取りやめました。登録する場合は「願い事をする」ともう一度いってください。")
NO_MSG = _("すみません。よく聞き取れませんでした。もう一度いってください。")
WISH_ADD_LIMIT_MSG = _(
    "すみません。現在、願い事は3つまでしか登録できません。次は何をしますか？"
)
WISH_LIST_NOT_PERSONALIZE = _(
    "すみません。誰の声か識別できませんでした。願い事の確認の際には音声プロフィールの登録が必要です。" \
    + "もう一度、「願い事を確認」とゆっくりと言ってみてください。" )
WISH_LIST_CHILD_MSG = _(
    "あなたが最後に登録した願い事は、{}、ですね。次は何をなさいますか？" \
    + "この願い事を削除するには次の四桁の暗号を言って下さい。<break time='500ms' />" \
    + "「<emphasis level='strong'><say-as interpret-as='digits'>{}</say-as></emphasis>」<break time='500ms' />です。" )
WISH_LIST_PARENT_MSG = _(
    "{} 番めの願い事は、" \
    + "<break time='500ms' />{}<break time='500ms' />です。" )
WISH_LIST_PARENT_EXT_MSG = _(
    "{} 番めの願い事は、" \
    + "<alexa:name type='first' personId='{}'/>さんの登録で、" \
    + "<break time='500ms' />{}<break time='500ms' />です。" )
WISH_LIST_NONE_CHILD_MSG = _("登録された願い事が確認できませんでした。" \
    + "まだ登録されていないか、音声識別が有効でない状態で登録されたのだと思われます。次は何をなさいますか？")
WISH_LIST_NONE_PARENT_MSG = _("まだ願い事が登録されていないようです。願い事が登録されるのを待ちましょう。次は何をなさいますか？")
WISH_DELETE_MSG = _(
    "登録されていた願い事を削除しました。次は何をしますか？"
)
WISH_DELETE_PARENT_MSG = _(
    "{} 番の願い事を削除しました。次は何をしますか？"
)
WISH_DELETE_NG_MSG = _(
    "すみません。登録されていた願い事の削除に失敗しました。もう一度「願い事を確認」からやり直してください。"
)
WISH_DELETE_NON_MSG = _(
    "すみません。願い事の削除の操作に失敗しました。もう一度「願い事を確認」からやり直してください。"
)
ANSWER_CLASS_LIMIT_MSG = _(
    "すみません。現在、願い事は3つまでしか登録できません。もっと登録したい場合には「プレミアム機能」の購入が必要になります。" \
    + "詳しく知りたい方は「プレミアム機能について教えて」と言ってみてください"
)
HELP_MSG = _(
    "{} はみんながサンタに願い事を登録し、サンタがその願い事を聞くスキルです。".format(SKILL_NAME) \
    + "使用するにはアレクサアプリで音声プロフィールの登録が必要です。でも、サンタの登録の後であれば音声プロフィールが登録されていなくても願い事の登録は行うことができます。" \
    + "願い事の登録は、「願い事を聞いて」。" \
    + "願い事の確認は、「願い事を確認」。音声プロフィールを有効にされている場合は願い事の確認のあとにお伝えする" \
    + "方法を使って、願い事を削除する事ができます。まずは削除したい「願い事を確認」して下さい。" \
    + "プレミアム機能について知りたい方は、「プレミアム機能について教えて」。" \
    + "のように遊んでください。何をしますか？" )
PREMIUM_INFO_MSG = _("私のサンタクローススキルは願い事を三つまで登録できるスキルです。" \
    + "プレミアム機能を購入する事によってその制限がなくなり、" \
    + "いくつでも登録ができるようになります。購入する場合には「プレミアム機能を購入」といってください")
SHOPPING_T_MSG = _(
    "すでにプレミアム機能が有効になっています。キャンセルする場合には「プレミアム機能をキャンセル」といってください")
SHOPPING_F_MSG = _(
    "プレミアム機能の購入はされていません。購入する場合には「プレミアム機能を購入」といってください")
GOODBYE_MSG = _("使ってくれてありがとう。ではまた")
REFLECTOR_MSG = _("You just triggered {}")
ERROR = _("すみません。よく聞き取れませんでした。もう一度お願いします。")
