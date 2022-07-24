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
    '''pre-content'''
    slice = content[:content.find('<h3')]
    while slice.find('<p>') != -1:
        pre.append(slice[slice.find('<p>')+3:slice.find('</p>')])
        slice = slice[slice.find('</p>')+4:]
    # print(pre)
    while content.find('<h3') != -1:
        content = content[content.find('<h3')+3:]
        content = content[content.find('>')+1:]
        titles.append(content[:content.find('</h3>')])
        content = content[content.find('</h3>')+5:]
        # print(content[content.find('<p>')+3:])
        part = content[:content[content.find('<p>')+3:].find('</div>')+content.find('<p>')+3]
        # print(part)
        ps = []
        while part.find('<p>') != -1:
            ps.append(part[part.find('<p>')+3:part.find('</p')])
            part = part[part.find('</p>')+4:]
            content = content[content.find('</p>')+4:]
        details.append(ps)
    # while content.find('<p>') != -1:

    # print(titles, details)
    # print(len(titles), len(details))
    return pre, titles, details

def web_process(**kwargs):
    pre, titles, details = get(**kwargs)
    htmllines = []
    # htmllines.append('[English](https://github.com/arielherself/espresso/blob/main/README.md)|[中文](https://github-com.translate.goog/arielherself/espresso/blob/main/README.md?_x_tr_sl=en&_x_tr_tl=zh-CN&_x_tr_hl=zh-CN&_x_tr_pto=wapp)\n\n')
    # htmllines.append('![The Economist](menubar.png)')
    prefix = '''
<!DOCTYPE html>
<html>
    <head>
        <style type="text/css">
            @font-face {
                font-family: 'custom';
                src: url('./milo-primary-subset-rg.woff2');
            } 
            div.customisedFont{
                font-family: 'custom';
                font-size:135%;
                line-height: 150%;
            }
        </style>
        <link rel="stylesheet" href="https://unpkg.com/mdui@1.0.2/dist/css/mdui.min.css"/>
        <link rel="shortcut icon" href="https://www.economist.com/engassets/ico/favicon.f1ea908894.ico" type="image/x-icon">
        <title>Espresso</title>
    </head>
    <body class="mdui-theme-primary-red mdui-color-theme mdui-typo mdui-theme-layout-auto">
        <div class="mdui-appbar mdui-appbar-fixed">
            <div class="mdui-toolbar mdui-color-theme">
              <a href="https://github.com/arielherself/espresso-native" class="mdui-btn mdui-btn-icon">
                <i class="mdui-icon material-icons">
                    <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 36 36" enable-background="new 0 0 36 36" xml:space="preserve" class="mdui-icon" style="width: 24px;height:24px;">
                        <path fill-rule="evenodd" clip-rule="evenodd" fill="#ffffff" d="M18,1.4C9,1.4,1.7,8.7,1.7,17.7c0,7.2,4.7,13.3,11.1,15.5c0.8,0.1,1.1-0.4,1.1-0.8c0-0.4,0-1.4,0-2.8c-4.5,1-5.5-2.2-5.5-2.2c-0.7-1.9-1.8-2.4-1.8-2.4c-1.5-1,0.1-1,0.1-1c1.6,0.1,2.5,1.7,2.5,1.7c1.5,2.5,3.8,1.8,4.7,1.4c0.1-1.1,0.6-1.8,1-2.2c-3.6-0.4-7.4-1.8-7.4-8.1c0-1.8,0.6-3.2,1.7-4.4c-0.2-0.4-0.7-2.1,0.2-4.3c0,0,1.4-0.4,4.5,1.7c1.3-0.4,2.7-0.5,4.1-0.5c1.4,0,2.8,0.2,4.1,0.5c3.1-2.1,4.5-1.7,4.5-1.7c0.9,2.2,0.3,3.9,0.2,4.3c1,1.1,1.7,2.6,1.7,4.4c0,6.3-3.8,7.6-7.4,8c0.6,0.5,1.1,1.5,1.1,3c0,2.2,0,3.9,0,4.5c0,0.4,0.3,0.9,1.1,0.8c6.5-2.2,11.1-8.3,11.1-15.5C34.3,8.7,27,1.4,18,1.4z"></path>
                    </svg>
                </i>
              </a>
              <a href="https://www.economist.com" class="mdui-typo-title"><b>T</b>he <b>E</b>conomist</a>
              <div class="mdui-toolbar-spacer"></div>
              <a href="javascript:location.reload();" class="mdui-btn mdui-btn-icon">
              <i class="mdui-icon material-icons">refresh</i>
              </a>
            </div>
        </div>
        <div class="mdui-container customisedFont mdui-typo" style="max-width: 700px;">
<br>
<div style="line-height: 70%;">
    <h1 align="center" class="mdui-typo-display-3"><strong>The world in brief</strong></h1>
    <p align="center" class="mdui-typo-headline">Catch up quickly on the global stories that matter</p>
    <p align="center" class="mdui-typo-subheading"><i>Origin: <a href="https://www.economist.com/the-world-in-brief">https://www.economist.com/the-world-in-brief</a></i><hr></p>
</div>
    '''
    htmllines.append(prefix)
    for each in pre:
        if each == '':
            continue
        processed_detail = each
        # while processed_detail.find('<strong>') != -1:
        #     if processed_detail[processed_detail.find('<strong>')-1] == ' ':
        #         if processed_detail[processed_detail.find('<strong>')+8] == ' ':
        #             processed_detail = processed_detail[:processed_detail.find('<strong>')]+'**'+processed_detail[processed_detail.find('<strong>')+9:]
        #         else:
        #             processed_detail = processed_detail[:processed_detail.find('<strong>')]+'**'+processed_detail[processed_detail.find('<strong>')+8:]
        #     else:
        #         if processed_detail[processed_detail.find('<strong>')+8] == ' ':
        #             processed_detail = processed_detail[:processed_detail.find('<strong>')]+' **'+processed_detail[processed_detail.find('<strong>')+9:]
        #         else:
        #             processed_detail = processed_detail[:processed_detail.find('<strong>')]+' **'+processed_detail[processed_detail.find('<strong>')+8:]
        # while processed_detail.find('</strong') != -1:
        #     if processed_detail[processed_detail.find('</strong>')+9] == ' ':
        #         if processed_detail[processed_detail.find('</strong>')-1] == ' ':
        #             processed_detail = processed_detail[:processed_detail.find('</strong>')-1]+'**'+processed_detail[processed_detail.find('</strong>')+9:]
        #         else:
        #             processed_detail = processed_detail[:processed_detail.find('</strong>')]+'**'+processed_detail[processed_detail.find('</strong>')+9:]
        #     else:
        #         if processed_detail[processed_detail.find('</strong>')-1] == ' ':
        #             processed_detail = processed_detail[:processed_detail.find('</strong>')-1]+'** '+processed_detail[processed_detail.find('</strong>')+9:]
        #         else:
        #             processed_detail = processed_detail[:processed_detail.find('</strong>')]+'** '+processed_detail[processed_detail.find('</strong>')+9:]
        # while processed_detail.find('<a ') != -1:
            # print(len(processed_detail))
            # print(processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6)
            # print(processed_detail[processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6:].find('"')+processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+1)
            # print(processed_detail[processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6:processed_detail[processed_detail[processed_detail.find("<a "):].find('href="'):].find('"')+processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+1])
            # processed_detail[processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6:processed_detail[processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6:].find('"')+processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+1]
            # exit(0)
        # while processed_detail.find('<a href="/') != -1:
        #     hyperlink = processed_detail[processed_detail[processed_detail.find("""<a href=\""""):].find('href="')+processed_detail.find("<a ")+6:processed_detail[processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6:].find('"')+processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6]
        #     print(processed_detail[processed_detail.find("<a "):])
        #     if hyperlink.startswith('//'):
        #         hyperlink = 'https:' + hyperlink
        #     elif hyperlink.startswith('/'):
        #         hyperlink = 'https://www.economist.com' + hyperlink
        #     print(hyperlink)
        #     processed_detail = processed_detail[:processed_detail.find('<a ')]+f'<a href="{hyperlink}">{processed_detail[processed_detail[processed_detail.find("<a "):].find(">")+processed_detail.find("<a ")+1:processed_detail[processed_detail.find("<a ")+1:].find("</a>")+processed_detail.find("<a ")+1]}</a>'+processed_detail[processed_detail.find('</a>')+4:]
        #     break
            # print(processed_detail)


            # print(processed_detail)
        # while processed_detail.find('<br/>') != -1:
        #     processed_detail = processed_detail[:processed_detail.find('<br/>')]+'  \n'+processed_detail[processed_detail.find('<br/>')+5:]
        processed_detail = processed_detail.replace('<a href="//', '<a href="https://').replace('<a href="/', '<a href="https://economist.com/')
        processed_detail = processed_detail.replace('<a ', '<a class="mdui-text-color-theme" ')
        htmllines.append(f'<p>{processed_detail}</p>')
    htmllines.append('<hr>')
    for i in range(len(titles)):
        htmllines.append(f'<h3>{titles[i]}</h3>')
        for j in range(len(details[i])):
            processed_detail = details[i][j]
            # while processed_detail.find('<strong>') != -1:
            #     if processed_detail[processed_detail.find('<strong>')-1] == ' ':
            #         if processed_detail[processed_detail.find('<strong>')+8] == ' ':
            #             processed_detail = processed_detail[:processed_detail.find('<strong>')]+'**'+processed_detail[processed_detail.find('<strong>')+9:]
            #         else:
            #             processed_detail = processed_detail[:processed_detail.find('<strong>')]+'**'+processed_detail[processed_detail.find('<strong>')+8:]
            #     else:
            #         if processed_detail[processed_detail.find('<strong>')-1] == ' ':
            #             processed_detail = processed_detail[:processed_detail.find('<strong>')]+' **'+processed_detail[processed_detail.find('<strong>')+9:]
            #         else:
            #             processed_detail = processed_detail[:processed_detail.find('<strong>')]+' **'+processed_detail[processed_detail.find('<strong>')+8:]
            # while processed_detail.find('</strong') != -1:
            #     if processed_detail[processed_detail.find('</strong>')+9] == ' ':
            #         if processed_detail[processed_detail.find('</strong>')-1] == ' ':
            #             processed_detail = processed_detail[:processed_detail.find('</strong>')-1]+'**'+processed_detail[processed_detail.find('</strong>')+9:]
            #         else:
            #             processed_detail = processed_detail[:processed_detail.find('</strong>')]+'**'+processed_detail[processed_detail.find('</strong>')+9:]
            #     else:
            #         if processed_detail[processed_detail.find('</strong>')-1] == ' ':
            #             processed_detail = processed_detail[:processed_detail.find('</strong>')-1]+'** '+processed_detail[processed_detail.find('</strong>')+9:]
            #         else:
            #             processed_detail = processed_detail[:processed_detail.find('</strong>')]+'** '+processed_detail[processed_detail.find('</strong>')+9:]
            # while processed_detail.find('<a ') != -1:
                # print(len(processed_detail))
                # print(processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6)
                # print(processed_detail[processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6:].find('"')+processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+1)
                # print(processed_detail[processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6:processed_detail[processed_detail[processed_detail.find("<a "):].find('href="'):].find('"')+processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+1])
                # processed_detail[processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6:processed_detail[processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6:].find('"')+processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+1]
                # exit(0)
            # while processed_detail.find('href="/') != -1:
            #     hyperlink = processed_detail[processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6:processed_detail[processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6:].find('"')+processed_detail[processed_detail.find("<a "):].find('href="')+processed_detail.find("<a ")+6]
            #     if hyperlink.startswith('//'):
            #         hyperlink = 'https:' + hyperlink
            #     elif hyperlink.startswith('/'):
            #         hyperlink = 'https://www.economist.com' + hyperlink
            #     processed_detail = processed_detail[:processed_detail.find('<a ')]+f'<a href={hyperlink}>{processed_detail[processed_detail[processed_detail.find("<a "):].find(">")+processed_detail.find("<a ")+1:processed_detail[processed_detail.find("<a ")+1:].find("</a>")+processed_detail.find("<a ")+1]}</a>'+processed_detail[processed_detail.find('</a>')+4:]
            #     break
                # print(processed_detail)
            # while processed_detail.find('<br/>') != -1:
            #     processed_detail = processed_detail[:processed_detail.find('<br/>')]+'  \n'+processed_detail[processed_detail.find('<br/>')+5:]
            processed_detail = processed_detail.replace('<a href="//', '<a href="https://').replace('<a href="/', '<a href="https://economist.com/')
            processed_detail = processed_detail.replace('<a ', '<a class="mdui-text-color-theme" ')
            htmllines.append(f'<p>{processed_detail}</p>')
    suffix = '''
    <hr>

<p><i>Owing to the difference between time zones of servers in which our auto-update script is running, content above probably doesn't match the one in your region.</i></p>

<br>'''
    proxy_suffix = '''
    <br> 
<div class="mdui-table-fluid" id="pop-up">
    <table class="mdui-table">
        <tbody>
            <tr>
                <td>
                    <div align="center"><img src="unlock.png" /><h1>Privacy Information</h1></div></br><p>We use a certain script to prevent the paywall from loading, thus links contained lead you to proxied corresponding webpages. Visiting these webpages means you have already acknowledged potential risks of having your behaviour recorded by Cloudflare.</p><br><br></div>
                    <div class="mdui-row-xs-2">
                        <div class="mdui-col">
                          <button class="mdui-btn mdui-btn-block mdui-color-theme-accent mdui-ripple" onclick="document.getElementById(`pop-up`).hidden=true">OK</button>
                        </div>
                        <div class="mdui-col">
                    <button class="mdui-btn mdui-btn-block mdui-color-theme-accent mdui-ripple">
                        <a href="raw.html">Visit the unmodified version</a>
                    </button>
                        </div>
                      </div>
                </td>
            </tr>
        </tbody>
    </table>
</div><br>'''
    general_suffix = '''
</div>
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
