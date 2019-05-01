<!DOCTYPE html>

<html  dir="ltr" lang="pl" xml:lang="pl">
<head>
    <title>ZAW: Wykład - Dopasowywanie wzorca</title>
    <link rel="shortcut icon" href="https://upel.agh.edu.pl/weaiib/theme/image.php/celupel/theme/1555284606/favicon" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="moodle, ZAW: Wykład - Dopasowywanie wzorca" />
<link rel="stylesheet" type="text/css" href="https://upel.agh.edu.pl/weaiib/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" /><script id="firstthemesheet" type="text/css">/** Required in order to fix style inclusion problems in IE with YUI **/</script><link rel="stylesheet" type="text/css" href="https://upel.agh.edu.pl/weaiib/theme/styles.php/celupel/1555284606_1555293767/all" />
<script type="text/javascript">
//<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/upel.agh.edu.pl\/weaiib","sesskey":"1w78Oz8kG9","themerev":"1555284606","slasharguments":1,"theme":"celupel","iconsystemmodule":"core\/icon_system_fontawesome","jsrev":"1555284606","admin":"admin","svgicons":true,"usertimezone":"Europa \/ Warszawa","contextid":46574};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''}
if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else{me.path=component+'/'+component+'.'+me.type}};
YUI_config = {"debug":false,"base":"https:\/\/upel.agh.edu.pl\/weaiib\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/upel.agh.edu.pl\/weaiib\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/upel.agh.edu.pl\/weaiib\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/upel.agh.edu.pl\/weaiib\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/upel.agh.edu.pl\/weaiib\/theme\/yui_combo.php?m\/1555284606\/","combine":true,"comboBase":"https:\/\/upel.agh.edu.pl\/weaiib\/theme\/yui_combo.php?","ext":false,"root":"m\/1555284606\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core-checknet":{"requires":["base-base","moodle-core-notification-alert","io-base"]},"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-languninstallconfirm":{"requires":["base","node","moodle-core-notification-confirm","moodle-core-notification-alert"]},"moodle-core-dock":{"requires":["base","node","event-custom","event-mouseenter","event-resize","escape","moodle-core-dock-loader","moodle-core-event"]},"moodle-core-dock-loader":{"requires":["escape"]},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-formchangechecker":{"requires":["base","event-focus","moodle-core-event"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core_availability-form":{"requires":["base","node","event","event-delegate","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-course-formatchooser":{"requires":["base","node","node-event-simulate"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-modchooser":{"requires":["moodle-core-chooserdialogue","moodle-course-coursebase"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-form-showadvanced":{"requires":["node","base","selector-css3"]},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-passwordunmask":{"requires":[]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-qbankmanager":{"requires":["node","selector-css3"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-qtype_ddimageortext-form":{"requires":["moodle-qtype_ddimageortext-dd","form_filepicker"]},"moodle-qtype_ddimageortext-dd":{"requires":["node","dd","dd-drop","dd-constrain"]},"moodle-qtype_ddmarker-form":{"requires":["moodle-qtype_ddmarker-dd","form_filepicker","graphics","escape"]},"moodle-qtype_ddmarker-dd":{"requires":["node","event-resize","dd","dd-drop","dd-constrain","graphics"]},"moodle-qtype_ddwtos-dd":{"requires":["node","dd","dd-drop","dd-constrain"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_attendance-groupfilter":{"requires":["base","node"]},"moodle-mod_forum-subscriptiontoggle":{"requires":["base-base","io-base"]},"moodle-mod_offlinequiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_offlinequiz-offlinequizbase","moodle-mod_offlinequiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_offlinequiz-repaginate":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_offlinequiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_offlinequiz-util","querystring-parse"]},"moodle-mod_offlinequiz-util":{"requires":["node"],"use":["moodle-mod_offlinequiz-util-base"],"submodules":{"moodle-mod_offlinequiz-util-base":{},"moodle-mod_offlinequiz-util-slot":{"requires":["node","moodle-mod_offlinequiz-util-base"]},"moodle-mod_offlinequiz-util-page":{"requires":["node","moodle-mod_offlinequiz-util-base"]}}},"moodle-mod_offlinequiz-offlinequizbase":{"requires":["base","node"]},"moodle-mod_offlinequiz-offlinequizquestionbank":{"requires":["base","event","node","io","io-form","yui-later","moodle-question-qbankmanager","moodle-core-notification-dialogue"]},"moodle-mod_offlinequiz-randomquestion":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_offlinequiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_offlinequiz-modform":{"requires":["base","node","event"]},"moodle-mod_offlinequiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_offlinequiz-offlinequizbase","moodle-mod_offlinequiz-util-base","moodle-mod_offlinequiz-util-page","moodle-mod_offlinequiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-repaginate":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-util":{"requires":["node","moodle-core-actionmenu"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","node-event-html5","node-event-simulate","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers","querystring-stringify"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers","moodle-editor_atto-menu"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_grader-gradereporttable":{"requires":["base","node","event","handlebars","overlay","event-hover"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_lp-dragdrop-reorder":{"requires":["moodle-core-dragdrop"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","transition","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-alert","moodle-core-notification-warning","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_html-button":{"requires":["moodle-editor_atto-plugin","event-valuechange"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin","moodle-form-shortforms"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_recordrtc-button":{"requires":["moodle-editor_atto-plugin","moodle-atto_recordrtc-recording"]},"moodle-atto_recordrtc-recording":{"requires":["moodle-atto_recordrtc-button"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/upel.agh.edu.pl\/weaiib\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/upel.agh.edu.pl\/weaiib\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1555284606\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/upel.agh.edu.pl\/weaiib\/lib\/javascript.php\/1555284606\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker","moodle-core-notification-dialogue"]},"core_comment":{"name":"core_comment","fullpath":"https:\/\/upel.agh.edu.pl\/weaiib\/lib\/javascript.php\/1555284606\/comment\/comment.js","requires":["base","io-base","node","json","yui2-animation","overlay","escape"]},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdnjs.cloudflare.com\/ajax\/libs\/mathjax\/2.7.2\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
</script>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-6375177-13"></script>
<script>
  window.dataLayer = window.dataLayer || []; 
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
 
  gtag('config', 'UA-6375177-13');
</script>
<meta name="robots" content="noindex" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	
	<script type="text/javascript" src="https://upel.agh.edu.pl/kokpit/cookies/cookies_utf-8_akcept.js"></script>

</head>
<body  id="page-mod-url-view" class="format-weeks  path-mod path-mod-url gecko dir-ltr lang-pl yui-skin-sam yui3-skin-sam upel-agh-edu-pl--weaiib pagelayout-incourse course-408 context-46574 cmid-19122 category-17 ">

<div id="page-wrapper">

    <div>
    <a class="sr-only sr-only-focusable" href="#maincontent">Przejdź do głównej zawartości</a>
</div><script type="text/javascript" src="https://upel.agh.edu.pl/weaiib/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js"></script><script type="text/javascript" src="https://upel.agh.edu.pl/weaiib/lib/javascript.php/1555284606/lib/javascript-static.js"></script>
<script type="text/javascript">
//<![CDATA[
document.body.className += ' jsenabled';
//]]>
</script>



    <nav class="fixed-top navbar navbar-light bg-white navbar-expand moodle-has-zindex">
    
            <div data-region="drawer-toggle" class="d-inline-block mr-3">
                <button aria-expanded="false" aria-controls="nav-drawer" type="button" class="btn nav-link float-sm-left mr-1 btn-secondary" data-action="toggle-drawer" data-side="left" data-preference="drawer-open-nav"><i class="icon fa fa-bars fa-fw " aria-hidden="true"  ></i><span class="sr-only">Panel boczny</span></button>
    	   </div>
    
    	   
    <div id="uczelnianaplatforma">
    			<span class="site-name d-none d-md-inline"><div id="kokpittop"><a href="http://upel.agh.edu.pl/kokpit/"><img class="startloginmain" src="https://upel.agh.edu.pl/weaiib/theme/image.php/celupel/theme/1555284606/images/kokpitupel" alt="Kokpit" height="33"></a></div></span>
    </div>	   
    	   
    	   
    	   
            <a href="https://upel.agh.edu.pl/weaiib" class="navbar-brand 
                    d-none d-sm-inline
                    ">
                <span class="site-name d-none d-md-inline">WEAiIB</span>
            </a>
    
            <ul class="navbar-nav d-md-flex">
                <!-- custom_menu -->
                <li class="dropdown nav-item">
    <a class="dropdown-toggle nav-link" id="drop-down-5cb45122483735cb4512246c374" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" href="#">
        Polski ‎(pl)‎
    </a>
    <div class="dropdown-menu" aria-labelledby="drop-down-5cb45122483735cb4512246c374">
                <a class="dropdown-item" href="https://upel.agh.edu.pl/weaiib/mod/url/view.php?id=19122&amp;lang=en" title="English ‎(en)‎">English ‎(en)‎</a>
                <a class="dropdown-item" href="https://upel.agh.edu.pl/weaiib/mod/url/view.php?id=19122&amp;lang=pl" title="Polski ‎(pl)‎">Polski ‎(pl)‎</a>
    </div>
</li> <!--  ukrycie menu jezykowego-->
                <!-- page_heading_menu -->
                
            </ul>
            <ul class="nav navbar-nav ml-auto">
                <div class="d-none d-lg-block">
                
            </div>
                <!-- navbar_plugin_output -->
                <li class="nav-item">
                <div class="popover-region collapsed popover-region-messages"
    id="nav-message-popover-container" data-userid="5749"
    data-region="popover-region">
    <div class="popover-region-toggle nav-link"
        data-region="popover-region-toggle"
        role="button"
        aria-controls="popover-region-container-5cb4512248fa15cb4512246c375"
        aria-haspopup="true"
        aria-label="Wyświetl okno bez nowych wiadomości"
        tabindex="0">
                <i class="icon fa fa-comment fa-fw "  title="Przełącz menu wiadomości" aria-label="Przełącz menu wiadomości"></i>
        <div class="count-container hidden" data-region="count-container">0</div>

    </div>
    <div 
        id="popover-region-container-5cb4512248fa15cb4512246c375"
        class="popover-region-container"
        data-region="popover-region-container"
        aria-expanded="false"
        aria-hidden="true"
        aria-label="Okno powiadomiemia"
        role="region">
        <div class="popover-region-header-container">
            <h3 class="popover-region-header-text" data-region="popover-region-header-text">Wiadomości</h3>
            <div class="popover-region-header-actions" data-region="popover-region-header-actions">        <div class="newmessage-link">
            <a href="https://upel.agh.edu.pl/weaiib/message/index.php?contactsfirst=1">Nowa wiadomość
            </a>
        </div>
        <a class="mark-all-read-button"
           href="#"
           role="button"
           title="Oznacz wszystko jako przeczytane"
           data-action="mark-all-read">
            <span class="normal-icon"><i class="icon fa fa-check fa-fw "  title="Oznacz wszystko jako przeczytane" aria-label="Oznacz wszystko jako przeczytane"></i></span>
            <span class="loading-icon"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Ładowanie" aria-label="Ładowanie"></i></span>
        </a>
        <a href="https://upel.agh.edu.pl/weaiib/message/edit.php?id=5749"
           title="Preferencje wiadomości">
            <i class="icon fa fa-cog fa-fw "  title="Preferencje wiadomości" aria-label="Preferencje wiadomości"></i>
        </a>
</div>
        </div>
        <div class="popover-region-content-container" data-region="popover-region-content-container">
            <div class="popover-region-content" data-region="popover-region-content">
                        <div class="messages" data-region="messages" role="log" aria-busy="false" aria-atomic="false" aria-relevant="additions"></div>
        <div class="empty-message" data-region="empty-message" tabindex="0">Brak oczekujących wiadomości</div>

            </div>
            <span class="loading-icon"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Ładowanie" aria-label="Ładowanie"></i></span>
        </div>
                <a class="see-all-link"
                    href="https://upel.agh.edu.pl/weaiib/message/index.php">
                    <div class="popover-region-footer-container">
                        <div class="popover-region-seeall-text">Wyświetl wszystko</div>
                    </div>
                </a>
    </div>
</div><div class="popover-region collapsed popover-region-notifications"
    id="nav-notification-popover-container" data-userid="5749"
    data-region="popover-region">
    <div class="popover-region-toggle nav-link"
        data-region="popover-region-toggle"
        role="button"
        aria-controls="popover-region-container-5cb451224acef5cb4512246c376"
        aria-haspopup="true"
        aria-label="Wyświetl okno bez nowych powiadomień"
        tabindex="0">
                <i class="icon fa fa-bell fa-fw "  title="Przełącz menu powiadomień" aria-label="Przełącz menu powiadomień"></i>
        <div class="count-container hidden" data-region="count-container">0</div>

    </div>
    <div 
        id="popover-region-container-5cb451224acef5cb4512246c376"
        class="popover-region-container"
        data-region="popover-region-container"
        aria-expanded="false"
        aria-hidden="true"
        aria-label="Okno powiadomiemia"
        role="region">
        <div class="popover-region-header-container">
            <h3 class="popover-region-header-text" data-region="popover-region-header-text">Powiadomienia</h3>
            <div class="popover-region-header-actions" data-region="popover-region-header-actions">        <a class="mark-all-read-button"
           href="#"
           title="Oznacz wszystko jako przeczytane"
           data-action="mark-all-read"
           role="button">
            <span class="normal-icon"><i class="icon fa fa-check fa-fw "  title="Oznacz wszystko jako przeczytane" aria-label="Oznacz wszystko jako przeczytane"></i></span>
            <span class="loading-icon"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Ładowanie" aria-label="Ładowanie"></i></span>
        </a>
        <a href="https://upel.agh.edu.pl/weaiib/message/notificationpreferences.php?userid=5749"
           title="Preferencje powiadomień">
            <i class="icon fa fa-cog fa-fw "  title="Preferencje powiadomień" aria-label="Preferencje powiadomień"></i>
        </a>
</div>
        </div>
        <div class="popover-region-content-container" data-region="popover-region-content-container">
            <div class="popover-region-content" data-region="popover-region-content">
                        <div class="all-notifications"
            data-region="all-notifications"
            role="log"
            aria-busy="false"
            aria-atomic="false"
            aria-relevant="additions"></div>
        <div class="empty-message" tabindex="0" data-region="empty-message">Nie masz powiadomień</div>

            </div>
            <span class="loading-icon"><i class="icon fa fa-circle-o-notch fa-spin fa-fw "  title="Ładowanie" aria-label="Ładowanie"></i></span>
        </div>
                <a class="see-all-link"
                    href="https://upel.agh.edu.pl/weaiib/message/output/popup/notifications.php">
                    <div class="popover-region-footer-container">
                        <div class="popover-region-seeall-text">Wyświetl wszystko</div>
                    </div>
                </a>
    </div>
</div>
                </li>
                <!-- user_menu -->
                <li class="nav-item d-flex align-items-center">
                    <div class="usermenu"><div class="action-menu moodle-actionmenu nowrap-items d-inline" id="action-menu-1" data-enhance="moodle-core-actionmenu">

        <div class="menubar d-flex " id="action-menu-1-menubar" role="menubar">

            


                <div class="action-menu-trigger">
                    <div class="dropdown">
                        <a href="#" class=" dropdown-toggle" id="dropdown-1" title="Menu użytkownika" role="menuitem" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            
                            <span class="userbutton"><span class="usertext mr-1">Gacek Daniel</span><span class="avatars"><span class="avatar current"><img src="https://upel.agh.edu.pl/weaiib/theme/image.php/celupel/core/1555284606/u/f2" class="userpicture defaultuserpic" width="35" height="35" role="presentation" aria-hidden="true" /></span></span></span>
                                
                            <b class="caret"></b>
                        </a>
                            <div class="dropdown-menu dropdown-menu-right menu  align-tr-br" id="action-menu-1-menu" data-rel="menu-content" aria-labelledby="action-menu-toggle-1" role="menu" data-align="tr-br">
                                        <a href="https://upel.agh.edu.pl/weaiib/my/" class="dropdown-item menu-action" role="menuitem" data-title="mymoodle,admin" aria-labelledby="actionmenuaction-1">
                                                <i class="icon fa fa-tachometer fa-fw " aria-hidden="true"  ></i>
                                            <span class="menu-action-text" id="actionmenuaction-1">
                                                Kokpit
                                            </span>
                                        </a>
                                        <div class="dropdown-divider"></div>
                                        <a href="https://upel.agh.edu.pl/weaiib/user/profile.php?id=5749" class="dropdown-item menu-action" role="menuitem" data-title="profile,moodle" aria-labelledby="actionmenuaction-2">
                                                <i class="icon fa fa-user fa-fw " aria-hidden="true"  ></i>
                                            <span class="menu-action-text" id="actionmenuaction-2">
                                                Profil
                                            </span>
                                        </a>
                                        <a href="https://upel.agh.edu.pl/weaiib/grade/report/overview/index.php" class="dropdown-item menu-action" role="menuitem" data-title="grades,grades" aria-labelledby="actionmenuaction-3">
                                                <i class="icon fa fa-table fa-fw " aria-hidden="true"  ></i>
                                            <span class="menu-action-text" id="actionmenuaction-3">
                                                Stopnie
                                            </span>
                                        </a>
                                        <a href="https://upel.agh.edu.pl/weaiib/message/index.php" class="dropdown-item menu-action" role="menuitem" data-title="messages,message" aria-labelledby="actionmenuaction-4">
                                                <i class="icon fa fa-comment fa-fw " aria-hidden="true"  ></i>
                                            <span class="menu-action-text" id="actionmenuaction-4">
                                                Wiadomości
                                            </span>
                                        </a>
                                        <a href="https://upel.agh.edu.pl/weaiib/user/preferences.php" class="dropdown-item menu-action" role="menuitem" data-title="preferences,moodle" aria-labelledby="actionmenuaction-5">
                                                <i class="icon fa fa-wrench fa-fw " aria-hidden="true"  ></i>
                                            <span class="menu-action-text" id="actionmenuaction-5">
                                                Ustawienia
                                            </span>
                                        </a>
                                        <div class="dropdown-divider"></div>
                                        <a href="https://upel.agh.edu.pl/weaiib/login/logout.php?sesskey=1w78Oz8kG9" class="dropdown-item menu-action" role="menuitem" data-title="logout,moodle" aria-labelledby="actionmenuaction-6">
                                                <i class="icon fa fa-sign-out fa-fw " aria-hidden="true"  ></i>
                                            <span class="menu-action-text" id="actionmenuaction-6">
                                                Wyloguj
                                            </span>
                                        </a>
                            </div>
                    </div>
                </div>

        </div>

</div></div>
                </li>
            </ul>
            <!-- search_box -->
    </nav>
    

    <div id="page" class="container-fluid">
        <header id="page-header" class="row">
    <div class="col-12 pt-3 pb-3">
        <div class="card">
            <div class="card-body">
                <div class="d-flex">
                    <div class="mr-auto">
                    <div class="page-context-header"><div class="page-header-headings"><h1>Zaawansowane Algorytmy Wizyjne</h1></div></div>
                    </div>

                </div>
                <div class="d-flex flex-wrap">
                    <div id="page-navbar">
                        <nav role="navigation">
    <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="https://upel.agh.edu.pl/weaiib/" >Strona główna</a></li>
                <li class="breadcrumb-item">Moje kursy</li>
                <li class="breadcrumb-item"><a href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408" title="Zaawansowane Algorytmy Wizyjne">ZAW</a></li>
                <li class="breadcrumb-item"><a href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408#section-8" >15 kwiecień - 21 kwiecień</a></li>
                <li class="breadcrumb-item"><a href="https://upel.agh.edu.pl/weaiib/mod/url/view.php?id=19122" title="Adres URL">Wykład - Dopasowywanie wzorca</a></li>
    </ol>
</nav>
                    </div>
                    <div class="ml-auto d-flex">
                        
                    </div>
                    <div id="course-header">
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>

        <div id="page-content" class="row">
            <div id="region-main-box" class="col-12">
                <section id="region-main" >
                    <div class="card">
                        <div class="card-body">
                            <span class="notifications" id="user-notifications"></span>
                            <div role="main"><span id="maincontent"></span><h2>Wykład - Dopasowywanie wzorca</h2><div class="urlworkaround">Kliknij link <a href="http://home.agh.edu.pl/~piotrus/ZAW/dop_wzor/siframes.html" >http://home.agh.edu.pl/~piotrus/ZAW/dop_wzor/siframes.html</a>, aby otworzyć zasób.</div></div>
                            <div class="m-t-2 m-b-1">
<div class="row">
    <div class="col-md-4">        <div class="pull-left">
                <a href="https://upel.agh.edu.pl/weaiib/mod/assign/view.php?id=19119&forceview=1" id="prev-activity-link" class="btn btn-link"  title="Wklejanie rozwiązań - Hough" >&#x25C4; Wklejanie rozwiązań - Hough</a>

        </div>
</div>
    <div class="col-md-4">        <div class="mdl-align">
            <div class="urlselect">
    <form method="post" action="https://upel.agh.edu.pl/weaiib/course/jumpto.php" class="form-inline" id="url_select_f5cb4512246c3715">
        <input type="hidden" name="sesskey" value="1w78Oz8kG9">
            <label for="jump-to-activity" class="sr-only">
                Przejdź do...
            </label>
        <select  id="jump-to-activity" class="custom-select urlselect" name="jump"
                 >
                    <option value="" selected>Przejdź do...</option>
                    <option value="/mod/forum/view.php?id=18290&amp;forceview=1" >Forum aktualności</option>
                    <option value="/mod/page/view.php?id=18291&amp;forceview=1" >Tematyka</option>
                    <option value="/mod/page/view.php?id=18357&amp;forceview=1" >Konfiguracja IDE/OpenCV</option>
                    <option value="/mod/resource/view.php?id=18358&amp;forceview=1" >mandril.jpg</option>
                    <option value="/mod/resource/view.php?id=18380&amp;forceview=1" >lena</option>
                    <option value="/mod/resource/view.php?id=18382&amp;forceview=1" >img seq</option>
                    <option value="/mod/resource/view.php?id=18383&amp;forceview=1" >skrypt zaw 04 03 2018</option>
                    <option value="/mod/resource/view.php?id=18408&amp;forceview=1" >REGULAMIN  LABORATORIUM SIECI NEURONOWYCH</option>
                    <option value="/mod/resource/view.php?id=18409&amp;forceview=1" >INSTRUKCJA BHP LABORATORIUM SIECI NEURONOWYCH</option>
                    <option value="/mod/resource/view.php?id=18454&amp;forceview=1" >Wykład - Segmentacja obiektów pierwszoplanowych</option>
                    <option value="/mod/resource/view.php?id=18469&amp;forceview=1" >Skrypt ZAW 04_03_2019</option>
                    <option value="/mod/folder/view.php?id=18467&amp;forceview=1" >Sekwencje testowe</option>
                    <option value="/mod/assign/view.php?id=18475&amp;forceview=1" >Wklejanie rozwiązań</option>
                    <option value="/mod/resource/view.php?id=18568&amp;forceview=1" >Wykład - Segmentacja obiektów pierwszoplanowych</option>
                    <option value="/mod/resource/view.php?id=18566&amp;forceview=1" >Instrukcja</option>
                    <option value="/mod/folder/view.php?id=18567&amp;forceview=1" >Sekwencje testowe</option>
                    <option value="/mod/assign/view.php?id=18569&amp;forceview=1" >Wklejanie rozwiązań - pierwszoplanowe</option>
                    <option value="/mod/assign/view.php?id=21833&amp;forceview=1" >Wklejanie rozwiązań - ViBE</option>
                    <option value="/mod/resource/view.php?id=18470&amp;forceview=1" >Background Segmentation with Feedback The Pixel-Based Adaptive Segmenter</option>
                    <option value="/mod/resource/view.php?id=18468&amp;forceview=1" >ViBe A Universal Background Subtraction Algorithm for Video Sequences</option>
                    <option value="/mod/resource/view.php?id=18573&amp;forceview=1" >Wykład - Przepływ Optyczny</option>
                    <option value="/mod/assign/view.php?id=21996&amp;forceview=1" >Kartkówka Tło</option>
                    <option value="/mod/resource/view.php?id=18603&amp;forceview=1" >Instrukcja - Przepływ optyczny</option>
                    <option value="/mod/assign/view.php?id=18604&amp;forceview=1" >Wklejanie rozwiązań - przepływ optyczny</option>
                    <option value="/mod/folder/view.php?id=18606&amp;forceview=1" >Pliki do przetwarzania</option>
                    <option value="/mod/url/view.php?id=18917&amp;forceview=1" >Wykład - Rzutowanie, kalibracja, stereowizja</option>
                    <option value="/mod/assign/view.php?id=21998&amp;forceview=1" >Kartkówka Przepływ optyczny</option>
                    <option value="/mod/resource/view.php?id=18941&amp;forceview=1" >Instrukcja</option>
                    <option value="/mod/resource/view.php?id=18940&amp;forceview=1" >calibration_stereo.zip</option>
                    <option value="/mod/assign/view.php?id=18946&amp;forceview=1" >Wklejanie rozwiązań - kalibracja</option>
                    <option value="/mod/url/view.php?id=19121&amp;forceview=1" >Wykład - Termowizja</option>
                    <option value="/mod/assign/view.php?id=21997&amp;forceview=1" >Kartkówka Kalibracja, stereowizja</option>
                    <option value="/mod/resource/view.php?id=22092&amp;forceview=1" >Instrukcja</option>
                    <option value="/mod/resource/view.php?id=19046&amp;forceview=1" >Test IR frame</option>
                    <option value="/mod/resource/view.php?id=19047&amp;forceview=1" >IR test sequence</option>
                    <option value="/mod/assign/view.php?id=19050&amp;forceview=1" >Wklejanie rozwiązań - Termowizja</option>
                    <option value="/mod/url/view.php?id=19120&amp;forceview=1" >Wykład - Rozpoznawanie kształtów</option>
                    <option value="/mod/resource/view.php?id=22122&amp;forceview=1" >Instrukcja</option>
                    <option value="/mod/resource/view.php?id=19002&amp;forceview=1" >Pliki do ćwiczeń</option>
                    <option value="/mod/assign/view.php?id=19001&amp;forceview=1" >Wklejanie rozwiązań - Hausdorff</option>
                    <option value="/mod/resource/view.php?id=22301&amp;forceview=1" >Instrukcja</option>
                    <option value="/mod/resource/view.php?id=19118&amp;forceview=1" >Pliki do ćwiczeń</option>
                    <option value="/mod/assign/view.php?id=19119&amp;forceview=1" >Wklejanie rozwiązań - Hough</option>
        </select>
            <noscript>
                <input type="submit" class="btn btn-secondary" value="Wykonaj">
            </noscript>
    </form>
</div>

        </div>
</div>
    <div class="col-md-4">        <div class="pull-right">
            
        </div>
</div>
</div>
</div>
                            
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </div>
    <div id="nav-drawer" data-region="drawer" class="d-print-none moodle-has-zindex closed" aria-hidden="true" tabindex="-1">
        <nav class="list-group">
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408" data-key="coursehome" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="60" data-nodetype="0" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" >
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-graduation-cap fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">ZAW</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/user/index.php?id=408" data-key="participants" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="90" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-users fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">Uczestnicy</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/badges/view.php?type=2&amp;id=408" data-key="badgesview" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="70" data-nodetype="0" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-shield fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">Odznaki</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/admin/tool/lp/coursecompetencies.php?courseid=408" data-key="competencies" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="70" data-nodetype="0" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-check-square-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">Kompetencje</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/grade/report/index.php?id=408" data-key="grades" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="70" data-nodetype="0" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-table fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">Oceny</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408#section-0" data-key="5569" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="30" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-folder-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">Główne składowe</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408#section-1" data-key="5570" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="30" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-folder-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">25 luty - 3 marzec</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408#section-2" data-key="5571" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="30" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-folder-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">4 marzec - 10 marzec</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408#section-3" data-key="5572" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="30" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-folder-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">11 marzec - 17 marzec</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408#section-4" data-key="5573" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="30" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-folder-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">18 marzec - 24 marzec</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408#section-5" data-key="5577" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="30" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-folder-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">25 marzec - 31 marzec</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408#section-6" data-key="5580" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="30" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-folder-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">1 kwiecień - 7 kwiecień</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408#section-7" data-key="5579" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="30" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-folder-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">8 kwiecień - 14 kwiecień</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action active" href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408#section-8" data-key="5581" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="30" data-nodetype="1" data-collapse="0" data-forceopen="1" data-isactive="1" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-folder-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body font-weight-bold">15 kwiecień - 21 kwiecień</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408#section-9" data-key="5574" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="30" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-folder-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">22 kwiecień - 28 kwiecień</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408#section-16" data-key="5578" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="30" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="408">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-folder-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">10 czerwiec - 16 czerwiec</span>
                    </div>
                </div>
            </a>
        </nav>
        <nav class="list-group m-t-1">
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/" data-key="home" data-isexpandable="0" data-indent="0" data-showdivider="1" data-type="1" data-nodetype="1" data-collapse="0" data-forceopen="1" data-isactive="0" data-hidden="0" data-preceedwithhr="0" >
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-home fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">Strona główna</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/my/" data-key="myhome" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="70" data-nodetype="0" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="home">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-tachometer fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">Kokpit</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/calendar/view.php?view=month&amp;course=408" data-key="calendar" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="60" data-nodetype="0" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="1">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-calendar fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">Kalendarz</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/user/files.php" data-key="privatefiles" data-isexpandable="0" data-indent="0" data-showdivider="0" data-type="70" data-nodetype="0" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="1">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-file-o fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">Prywatne pliki</span>
                    </div>
                </div>
            </a>
            <div class="list-group-item" data-key="mycourses" data-isexpandable="1" data-indent="0" data-showdivider="0" data-type="0" data-nodetype="1" data-collapse="0" data-forceopen="1" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="home">
                <div class="m-l-0">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-graduation-cap fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body">Moje kursy</span>
                    </div>
                </div>
            </div>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=121" data-key="121" data-isexpandable="1" data-indent="1" data-showdivider="0" data-type="20" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="mycourses">
                <div class="m-l-1">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-graduation-cap fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">INPG</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=512" data-key="512" data-isexpandable="1" data-indent="1" data-showdivider="0" data-type="20" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="mycourses">
                <div class="m-l-1">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-graduation-cap fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">ml2019</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408" data-key="408" data-isexpandable="1" data-indent="1" data-showdivider="0" data-type="20" data-nodetype="1" data-collapse="0" data-forceopen="1" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="mycourses">
                <div class="m-l-1">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-graduation-cap fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">ZAW</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=146" data-key="146" data-isexpandable="1" data-indent="1" data-showdivider="0" data-type="20" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="mycourses">
                <div class="m-l-1">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-graduation-cap fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">PSRA</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=497" data-key="497" data-isexpandable="1" data-indent="1" data-showdivider="0" data-type="20" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="mycourses">
                <div class="m-l-1">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-graduation-cap fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">POWER WEAIiIB</span>
                    </div>
                </div>
            </a>
            <a class="list-group-item list-group-item-action " href="https://upel.agh.edu.pl/weaiib/course/view.php?id=130" data-key="130" data-isexpandable="1" data-indent="1" data-showdivider="0" data-type="20" data-nodetype="1" data-collapse="0" data-forceopen="0" data-isactive="0" data-hidden="0" data-preceedwithhr="0" data-parent-key="mycourses">
                <div class="m-l-1">
                    <div class="media">
                        <span class="media-left">
                            <i class="icon fa fa-graduation-cap fa-fw " aria-hidden="true"  ></i>
                        </span>
                        <span class="media-body ">PKSS</span>
                    </div>
                </div>
            </a>
        </nav>
    </div>
</div>

<footer id="page-footer" class="py-3 bg-dark text-light">
    <div class="container">
        <div id="course-footer"></div>
		
		
		<div id="uczelnianaplatforma">
<p style="text-align: center;">
<a href="http://upel.agh.edu.pl/kokpit/obszary.html" target="_blank"><img class="startlogin2" src="https://upel.agh.edu.pl/weaiib/theme/image.php/celupel/theme/1555284606/images/kokpit" alt="Obszary" height="60"></a>
<a href="http://upel.agh.edu.pl/kokpit/wtyczki.html" target="_blank"><img class="startlogin2" src="https://upel.agh.edu.pl/weaiib/theme/image.php/celupel/theme/1555284606/images/wtyczki" alt="Wtyczki" height="60"></a>
<a href="http://upel.agh.edu.pl/kokpit/faq.html" target="_blank"><img class="startlogin2" src="https://upel.agh.edu.pl/weaiib/theme/image.php/celupel/theme/1555284606/images/faq" alt="FAQ" height="60"></a>
</p>
</div>		
<p style="text-align: center; color: #009c58;"><a href="http://www.agh.edu.pl" target="_blank"> <img src="https://upel.agh.edu.pl/weaiib/theme/image.php/celupel/theme/1555284606/images/logoagh_grey" alt="logo AGH" width="60" height="87"></a> <a href="http://www.cel.agh.edu.pl" target="_blank"> <img src="https://upel.agh.edu.pl/weaiib/theme/image.php/celupel/theme/1555284606/images/logocel_grey" alt="logo CeL" width="73" height="87"></a> <a href="http://www.uci.agh.edu.pl/uci" target="_blank"> <img src="https://upel.agh.edu.pl/weaiib/theme/image.php/celupel/theme/1555284606/images/logouci_grey" alt="logo UCI" width="85" height="87"></a> <br />Platforma e-Learningowa obsługiwana jest przez: <br /> <a href="http://www.cel.agh.edu.pl" target="_blank">Centrum e-Learningu AGH</a> oraz <a href="http://www.uci.agh.edu.pl/uci" target="_blank"> Uczelniane Centrum Informatyki AGH</a><br /><br /><br /></p>
		
	
		
		
	<!--     ukrycie menu dolnego -->	

    <!--    
        <div class="logininfo">Jesteś zalogowany(a) jako <a href="https://upel.agh.edu.pl/weaiib/user/profile.php?id=5749" title="Zobacz profil">Gacek Daniel</a> (<a href="https://upel.agh.edu.pl/weaiib/login/logout.php?sesskey=1w78Oz8kG9">Wyloguj</a>)</div>
        <div class="tool_usertours-resettourcontainer"></div>
        <div class="homelink"><a href="https://upel.agh.edu.pl/weaiib/course/view.php?id=408">ZAW</a></div>
        <nav class="nav navbar-nav d-md-none">
                <ul class="list-unstyled pt-3">
                                    <li><a href="#" title="Język">Polski ‎(pl)‎</a></li>
                                <li>
                                    <ul class="list-unstyled ml-3">
                                                        <li><a href="https://upel.agh.edu.pl/weaiib/mod/url/view.php?id=19122&amp;lang=en" title="English ‎(en)‎">English ‎(en)‎</a></li>
                                                        <li><a href="https://upel.agh.edu.pl/weaiib/mod/url/view.php?id=19122&amp;lang=pl" title="Polski ‎(pl)‎">Polski ‎(pl)‎</a></li>
                                    </ul>
                                </li>
                </ul>
        </nav>
		-->
	<!--     ukrycie menu dolnego koniec -->		
        
		<center>
		<div class="tool_dataprivacy"><a href="https://upel.agh.edu.pl/weaiib/admin/tool/dataprivacy/summary.php">Podsumowanie przechowywania danych</a></div><a href="https://download.moodle.org/mobile?version=2018051705.06&amp;lang=pl&amp;iosappid=633359593&amp;androidappid=com.moodle.moodlemobile">Pobierz aplikację mobilną</a>
        <script type="text/javascript">
//<![CDATA[
var require = {
    baseUrl : 'https://upel.agh.edu.pl/weaiib/lib/requirejs.php/1555284606/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,
    waitSeconds : 0,

    paths: {
        jquery: 'https://upel.agh.edu.pl/weaiib/lib/javascript.php/1555284606/lib/jquery/jquery-3.2.1.min',
        jqueryui: 'https://upel.agh.edu.pl/weaiib/lib/javascript.php/1555284606/lib/jquery/ui-1.12.1/jquery-ui.min',
        jqueryprivate: 'https://upel.agh.edu.pl/weaiib/lib/javascript.php/1555284606/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },
      // Stub module for 'process'. This is a workaround for a bug in MathJax (see MDL-60458).
      '*': { process: 'core/first' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
</script>
<script type="text/javascript" src="https://upel.agh.edu.pl/weaiib/lib/javascript.php/1555284606/lib/requirejs/require.min.js"></script>
<script type="text/javascript">
//<![CDATA[
require(['core/first'], function() {
;
require(["media_videojs/loader"], function(loader) {
    loader.setUp(function(videojs) {
        videojs.options.flash.swf = "https://upel.agh.edu.pl/weaiib/media/player/videojs/videojs/video-js.swf";
videojs.addLanguage("pl",{
 "Play": "Odtwarzaj",
 "Pause": "Pauza",
 "Current Time": "Aktualny czas",
 "Duration Time": "Czas trwania",
 "Remaining Time": "Pozostały czas",
 "Stream Type": "Typ strumienia",
 "LIVE": "NA ŻYWO",
 "Loaded": "Załadowany",
 "Progress": "Status",
 "Fullscreen": "Pełny ekran",
 "Non-Fullscreen": "Pełny ekran niedostępny",
 "Mute": "Wyłącz dźwięk",
 "Unmute": "Włącz dźwięk",
 "Playback Rate": "Szybkość odtwarzania",
 "Subtitles": "Napisy",
 "subtitles off": "Napisy wyłączone",
 "Captions": "Transkrypcja",
 "captions off": "Transkrypcja wyłączona",
 "Chapters": "Rozdziały",
 "You aborted the media playback": "Odtwarzanie zostało przerwane",
 "A network error caused the media download to fail part-way.": "Problemy z siecią spowodowały błąd przy pobieraniu materiału wideo.",
 "The media could not be loaded, either because the server or network failed or because the format is not supported.": "Materiał wideo nie może być załadowany, ponieważ wystąpił problem z siecią lub format nie jest obsługiwany",
 "The media playback was aborted due to a corruption problem or because the media used features your browser did not support.": "Odtwarzanie materiału wideo zostało przerwane z powodu uszkodzonego pliku wideo lub z powodu błędu funkcji, które nie są wspierane przez przeglądarkę.",
 "No compatible source was found for this media.": "Dla tego materiału wideo nie znaleziono kompatybilnego źródła.",
 "Play video": "Odtwarzaj wideo",
 "Close": "Zamknij",
 "Modal Window": "Okno Modala",
 "This is a modal window": "To jest okno modala",
 "This modal can be closed by pressing the Escape key or activating the close button.": "Ten modal możesz zamknąć naciskając przycisk Escape albo wybierając przycisk Zamknij.",
 ", opens captions settings dialog": ", otwiera okno dialogowe ustawień transkrypcji",
 ", opens subtitles settings dialog": ", otwiera okno dialogowe napisów",
 ", selected": ", zaznaczone"
});

    });
});;

require(['jquery'], function($) {
    $('#single_select5cb4512246c373').change(function() {
        var ignore = $(this).find(':selected').attr('data-ignore');
        if (typeof ignore === typeof undefined) {
            $('#single_select_f5cb4512246c372').submit();
        }
    });
});
;

require(['jquery', 'message_popup/message_popover_controller'], function($, controller) {
    var container = $('#nav-message-popover-container');
    var controller = new controller(container);
    controller.registerEventListeners();
    controller.registerListNavigationEventListeners();
});
;

require(['jquery', 'message_popup/notification_popover_controller'], function($, controller) {
    var container = $('#nav-notification-popover-container');
    var controller = new controller(container);
    controller.registerEventListeners();
    controller.registerListNavigationEventListeners();
});
;

        require(['jquery'], function($) {
            $('#jump-to-activity').change(function() {
                if (!$(this).val()) {
                    return false;
                }
                $('#url_select_f5cb4512246c3715').submit();
            });
        });
    ;

require(['jquery'], function($) {
    $('#single_select5cb4512246c3717').change(function() {
        var ignore = $(this).find(':selected').attr('data-ignore');
        if (typeof ignore === typeof undefined) {
            $('#single_select_f5cb4512246c3716').submit();
        }
    });
});
;

require(['theme_celupel/loader']);
require(['theme_celupel/drawer'], function(mod) {
    mod.init();
});
;
require(["core/notification"], function(amd) { amd.init(46574, []); });;
require(["core/log"], function(amd) { amd.setConfig({"level":"warn"}); });
});
//]]>
</script>
<script type="text/javascript">
//<![CDATA[
M.str = {"moodle":{"lastmodified":"Ostatnia modyfikacja","name":"Nazwa","error":"B\u0142\u0105d","info":"Informacja","yes":"Tak","no":"Nie","cancel":"Anuluj","confirm":"Potwierd\u017a","areyousure":"Jeste\u015b pewien?","closebuttontitle":"Zamknij","unknownerror":"Nieznany b\u0142\u0105d"},"repository":{"type":"Typ","size":"Rozmiar","invalidjson":"Nieprawid\u0142owy ci\u0105g jSON","nofilesattached":"Nie za\u0142\u0105czono plik\u00f3w","filepicker":"Wyb\u00f3r plik\u00f3w","logout":"Wyloguj si\u0119","nofilesavailable":"Brak dost\u0119pnych plik\u00f3w","norepositoriesavailable":"Niestety, \u017cadne z istniej\u0105cych repozytori\u00f3w nie mo\u017ce zawiera\u0107 plik\u00f3w w wymaganym formacie.","fileexistsdialogheader":"Plik istnieje","fileexistsdialog_editor":"Plik o wybranej nazwie zosta\u0142 ju\u017c za\u0142\u0105czony do tekstu, kt\u00f3ry edytujesz.","fileexistsdialog_filemanager":"Plik o wybranej nazwie ju\u017c zosta\u0142 do\u0142\u0105czony","renameto":"Zmie\u0144 nazw\u0119 na","referencesexist":"Istnieje {$a} skr\u00f3t\u00f3w, kt\u00f3re wykorzystuj\u0105 ten plik jako \u017ar\u00f3d\u0142o.","select":"Wybierz"},"admin":{"confirmdeletecomments":"Zamierzasz usun\u0105\u0107 komentarze, czy jeste\u015b pewien(a)?","confirmation":"Potwierdzenie"}};
//]]>
</script>
<script type="text/javascript">
//<![CDATA[
(function() {Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"pl"});
});
M.util.help_popups.setup(Y);
 M.util.js_pending('random5cb4512246c3718'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random5cb4512246c3718'); });
})();
//]]>
</script>

		</center>
    </div>
</footer>
</body>
</html>