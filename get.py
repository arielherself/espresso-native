import requests
import datetime

MIRROR = 'te.arielherself.xyz'

def get(proxy=False, http_proxy='', https_proxy=''):
    try:
        if proxy:
            raw = requests.get('https://www.economist.com/the-world-in-brief', proxies={'http': http_proxy, 'https': https_proxy})
        else:
            raw = requests.get('https://www.economist.com/the-world-in-brief')
    except:
        return None #####################################
    content = raw.text
    pre = []
    details = []
    titles = []
    slice = content[:content.find('<h3')]
    while slice.find('<p>') != -1:
        pre.append(slice[slice.find('<p>')+3:slice.find('</p>')])
        slice = slice[slice.find('</p>')+4:]
    while content.find('<h3') != -1:
        content = content[content.find('<h3')+3:]
        content = content[content.find('>')+1:]
        titles.append(content[:content.find('</h3>')])
        content = content[content.find('</h3>')+5:]
        part = content[:content[content.find('<p>')+3:].find('</div>')+content.find('<p>')+3]
        ps = []
        while part.find('<p>') != -1:
            ps.append(part[part.find('<p>')+3:part.find('</p')])
            part = part[part.find('</p>')+4:]
            content = content[content.find('</p>')+4:]
        details.append(ps)
    return pre, titles, details

def web_process(**kwargs):
    pre, titles, details = get(**kwargs)
    htmllines = []
    prefix = '''
<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, shrink-to-fit=no">
        <style type="text/css">
            @font-face {
                font-family: 'custom';
                src: url('./milo-primary-subset-rg.woff2');
            } 
            div.customisedFont{
                font-family: 'custom';
                font-size:115%;
                line-height: 150%;
            }
        </style>
        <link rel="stylesheet" href="mdui-v1.0.2/css/mdui.min.css"/>
        <link rel="shortcut icon" href="https://www.economist.com/engassets/ico/favicon.f1ea908894.ico" type="image/x-icon">
        <title>Espresso</title>
    </head>
    <body class="mdui-theme-primary-red mdui-color-theme mdui-typo mdui-theme-layout-auto">
        <button mdui-dialog="{target: '#dialog'}" id="hidden_dialog" hidden></button>
        <div class="mdui-appbar mdui-appbar-fixed">
            <div class="mdui-toolbar mdui-color-red-a700">
              <a href="https://github.com/arielherself/espresso-native" class="mdui-btn mdui-btn-icon" mdui-tooltip="{content: 'Project repository', position: 'right'}">
                <i class="mdui-icon material-icons">
                    <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 36 36" enable-background="new 0 0 36 36" xml:space="preserve" class="mdui-icon" style="width: 24px;height:24px;">
                        <path fill-rule="evenodd" clip-rule="evenodd" fill="#ffffff" d="M18,1.4C9,1.4,1.7,8.7,1.7,17.7c0,7.2,4.7,13.3,11.1,15.5c0.8,0.1,1.1-0.4,1.1-0.8c0-0.4,0-1.4,0-2.8c-4.5,1-5.5-2.2-5.5-2.2c-0.7-1.9-1.8-2.4-1.8-2.4c-1.5-1,0.1-1,0.1-1c1.6,0.1,2.5,1.7,2.5,1.7c1.5,2.5,3.8,1.8,4.7,1.4c0.1-1.1,0.6-1.8,1-2.2c-3.6-0.4-7.4-1.8-7.4-8.1c0-1.8,0.6-3.2,1.7-4.4c-0.2-0.4-0.7-2.1,0.2-4.3c0,0,1.4-0.4,4.5,1.7c1.3-0.4,2.7-0.5,4.1-0.5c1.4,0,2.8,0.2,4.1,0.5c3.1-2.1,4.5-1.7,4.5-1.7c0.9,2.2,0.3,3.9,0.2,4.3c1,1.1,1.7,2.6,1.7,4.4c0,6.3-3.8,7.6-7.4,8c0.6,0.5,1.1,1.5,1.1,3c0,2.2,0,3.9,0,4.5c0,0.4,0.3,0.9,1.1,0.8c6.5-2.2,11.1-8.3,11.1-15.5C34.3,8.7,27,1.4,18,1.4z"></path>
                    </svg>
                </i>
              </a>
              <a href="https://www.economist.com" class="mdui-typo-title" mdui-tooltip="{content: 'Visit the official website', position: 'bottom'}"><b>T</b>he <b>E</b>conomist</a>
              <div class="mdui-toolbar-spacer"></div>
              <a href="javascript:location.reload();" class="mdui-btn mdui-btn-icon" mdui-tooltip="{content: 'Reload (Ctrl+R)', position: 'left'}">
              <i class="mdui-icon material-icons">refresh</i>
              </a>
            </div>
        </div>
        <div class="mdui-container customisedFont mdui-typo" style="max-width: 768px;">
<br><br>
<div>
    <h1 align="center" class="mdui-typo-display-3"><strong>The world in brief</strong></h1>
    <div align="center" class="mdui-typo-headline">Catch up quickly on the global stories that matter</div>
    <div align="center" class="mdui-typo-subheading"><i>Origin: <a href="https://www.economist.com/the-world-in-brief">https://www.economist.com/the-world-in-brief</a></i><hr></div>
</div>
<div class="mdui-container customisedFont mdui-typo" style="max-width: 768px;">
    <div class="mdui-row">
        <div class="mdui-col-xs-10">
            <div class="mdui-textfield mdui-textfield-expandable">
                <button class="mdui-textfield-icon mdui-btn mdui-btn-icon" mdui-tooltip="{content: 'Go to article...'}" onclick="document.getElementById(`submit_button`).hidden=true;">
                  <i class="mdui-icon material-icons">search</i>
                </button>
                <input class="mdui-textfield-input" type="text" placeholder="YYYY-MM-DD" id="targ" />
                <button class="mdui-textfield-close mdui-btn mdui-btn-icon" onclick="document.getElementById(`submit_button`).hidden=false;">
                  <i class="mdui-icon material-icons" mdui-tooltip="{content: 'Cancel'}">close</i>
                </button>
              </div>    
        </div>
        <div class="mdui-col-xs-2">
            <button class="mdui-btn mdui-color-red-a700" id="submit_button" hidden onclick="window.open(`archive/`+document.getElementById(`targ`).value)+`.html`;">Go</button>
        </div>
    </div>
    '''
    htmllines.append(prefix)
    for each in pre:
        if each == '':
            continue
        processed_detail = each
        processed_detail = processed_detail.replace('<a href="//', '<a href="https://').replace('<a href="/', '<a href="https://economist.com/')
        processed_detail = processed_detail.replace('<a ', '<a class="mdui-text-color-red-a700" ')
        htmllines.append(f'<p>{processed_detail}</p>')
    htmllines.append('<hr>')
    for i in range(len(titles)):
        htmllines.append(f'<h3>{titles[i]}</h3>')
        for j in range(len(details[i])):
            processed_detail = details[i][j]
            processed_detail = processed_detail.replace('<a href="//', '<a href="https://').replace('<a href="/', '<a href="https://economist.com/')
            processed_detail = processed_detail.replace('<a ', '<a class="mdui-text-color-red-a700" ')
            htmllines.append(f'<p>{processed_detail}</p>')
    suffix = '''
    <hr>

<p><i>Owing to the difference between time zones of servers in which our auto-update script is running, content above probably doesn't match the one in your region.</i></p>

<br></div>'''
    proxy_suffix = '''
    <div class="mdui-dialog" id="dialog">
        <div class="mdui-dialog-content">
            <div class="mdui-table-fluid" id="pop-up">
                <table class="mdui-table">
                    <tbody>
                        <tr>
                            <td>
                                <div align="center"><img src="unlock.png" /><h1>Privacy Information</h1></div><br><p>We use a certain script to prevent the paywall from loading, thus links contained lead you to proxied corresponding webpages. Visiting these webpages means you have already acknowledged potential risks of having your behaviour recorded by Cloudflare.</p><br><br></div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="mdui-dialog-actions">
          <button class="mdui-btn mdui-text-color-theme-text mdui-ripple" mdui-dialog-close onclick="window.open(`raw.html`);">Visit an unmodified version</button>
          <button class="mdui-btn mdui-ripple" mdui-dialog-confirm>OK</button>
        </div>
      </div>
      <script type="text/javascript">
    function click_button () {
        state = {title:'',url:window.location.href};
        history.pushState(state, '');
        document.getElementById(`hidden_dialog`).click();
    }
    window.onload = click_button;
    </script>

'''
    general_suffix = '''
<script src="mdui-v1.0.2/js/mdui.min.js"></script>
</body>
</html>'''
    htmllines.append(suffix)
    htmllines_proxied = [each.replace('www.economist.com', MIRROR).replace('economist.com', MIRROR) for each in htmllines]
    htmllines_proxied.append(proxy_suffix)
    htmllines_proxied.append(general_suffix)
    htmllines.append(general_suffix)
    return htmllines, htmllines_proxied

if __name__ == '__main__':
    page_raw, page = web_process(proxy=False)
    with open('index.html', 'w', encoding='utf8') as fil:
        print(*page, file=fil)
    with open('raw.html', 'w', encoding='utf8') as fil:
        print(*page_raw, file=fil)
    with open(f'archive/{datetime.datetime.now().isoformat()[:10]}.html', 'w', encoding='utf8') as fil:
        print(*page, file=fil)
