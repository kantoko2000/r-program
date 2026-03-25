import url from 'url';
import { createRunner } from '@puppeteer/replay';

export async function run(extension) {
    const runner = await createRunner(extension);

    await runner.runBeforeAllSteps();

    await runner.runStep({
        type: 'setViewport',
        width: 1092,
        height: 728,
        deviceScaleFactor: 1,
        isMobile: false,
        hasTouch: false,
        isLandscape: false
    });
    await runner.runStep({
        type: 'navigate',
        url: 'https://adfs.jp.ricoh.com/adfs/ls/',
        assertedEvents: [
            {
                type: 'navigation',
                url: 'https://adfs.jp.ricoh.com/adfs/ls/',
                title: 'サインイン'
            }
        ]
    });
    await runner.runStep({
        type: 'click',
        target: 'main',
        selectors: [
            [
                '#userNameInput'
            ],
            [
                'xpath///*[@id="userNameInput"]'
            ],
            [
                'pierce/#userNameInput'
            ],
            [
                'text/kosaku.saito@jp.ricoh.com'
            ]
        ],
        offsetY: 11.199996948242188,
        offsetX: 198,
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'a'
    });
    await runner.runStep({
        type: 'keyUp',
        key: 'a',
        target: 'main'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'c'
    });
    await runner.runStep({
        type: 'keyUp',
        key: 'Control',
        target: 'main'
    });
    await runner.runStep({
        type: 'keyUp',
        key: 'c',
        target: 'main'
    });
    await runner.runStep({
        type: 'click',
        target: 'main',
        selectors: [
            [
                '#userNameInput'
            ],
            [
                'xpath///*[@id="userNameInput"]'
            ],
            [
                'pierce/#userNameInput'
            ],
            [
                'text/kosaku.saito@jp.ricoh.com'
            ]
        ],
        offsetY: 13.199996948242188,
        offsetX: 197,
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'a'
    });
    await runner.runStep({
        type: 'keyUp',
        key: 'a',
        target: 'main'
    });
    await runner.runStep({
        type: 'change',
        value: 'kosaku.saito@jp.ricoh.com',
        selectors: [
            [
                '#userNameInput'
            ],
            [
                'xpath///*[@id="userNameInput"]'
            ],
            [
                'pierce/#userNameInput'
            ],
            [
                'text/kosaku.saito@jp.ricoh.com'
            ]
        ],
        target: 'main'
    });
    await runner.runStep({
        type: 'keyUp',
        key: 'Control',
        target: 'main'
    });
    await runner.runStep({
        type: 'click',
        target: 'main',
        selectors: [
            [
                '#passwordInput'
            ],
            [
                'xpath///*[@id="passwordInput"]'
            ],
            [
                'pierce/#passwordInput'
            ],
            [
                'text/zaq12wsxcde3'
            ]
        ],
        offsetY: 15.599990844726562,
        offsetX: 66,
    });
    await runner.runStep({
        type: 'click',
        target: 'main',
        selectors: [
            [
                '#passwordInput'
            ],
            [
                'xpath///*[@id="passwordInput"]'
            ],
            [
                'pierce/#passwordInput'
            ],
            [
                'text/zaq12wsxcde3'
            ]
        ],
        offsetY: 13.599990844726562,
        offsetX: 82,
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Alt'
    });
    await runner.runStep({
        type: 'keyUp',
        key: 'Alt',
        target: 'main'
    });
    await runner.runStep({
        type: 'click',
        target: 'main',
        selectors: [
            [
                '#passwordInput'
            ],
            [
                'xpath///*[@id="passwordInput"]'
            ],
            [
                'pierce/#passwordInput'
            ],
            [
                'text/zaq12wsxcde3'
            ]
        ],
        offsetY: 19.599990844726562,
        offsetX: 98,
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'a'
    });
    await runner.runStep({
        type: 'keyUp',
        key: 'a',
        target: 'main'
    });
    await runner.runStep({
        type: 'change',
        value: 'zaq12wsxcde3',
        selectors: [
            [
                '#passwordInput'
            ],
            [
                'xpath///*[@id="passwordInput"]'
            ],
            [
                'pierce/#passwordInput'
            ],
            [
                'text/zaq12wsxcde3'
            ]
        ],
        target: 'main'
    });
    await runner.runStep({
        type: 'keyUp',
        key: 'Control',
        target: 'main'
    });
    await runner.runStep({
        type: 'click',
        target: 'main',
        selectors: [
            [
                'aria/サインイン'
            ],
            [
                '#submitButton'
            ],
            [
                'xpath///*[@id="submitButton"]'
            ],
            [
                'pierce/#submitButton'
            ]
        ],
        offsetY: 11.199981689453125,
        offsetX: 77,
        assertedEvents: [
            {
                type: 'navigation',
                url: 'https://adfs.jp.ricoh.com/adfs/ls/?client-request-id=c88d0961-ae4f-4122-2401-00800c1c00ca',
                title: ''
            }
        ]
    });
    await runner.runStep({
        type: 'click',
        target: 'main',
        selectors: [
            [
                'aria/選択[role="button"]'
            ],
            [
                'input'
            ],
            [
                'xpath//html/body/form/table[3]/tbody/tr/td[4]/input'
            ],
            [
                'pierce/input'
            ]
        ],
        offsetY: 15,
        offsetX: 21,
        assertedEvents: [
            {
                type: 'navigation',
                url: 'https://www.vo3is.ricoh.co.jp/portal/companySelectAction.do',
                title: ''
            }
        ]
    });
    await runner.runStep({
        type: 'click',
        target: 'main',
        selectors: [
            [
                'aria/同意する[role="button"]'
            ],
            [
                'td:nth-of-type(2) > input'
            ],
            [
                'xpath//html/body/form/table[2]/tbody/tr/td[2]/input'
            ],
            [
                'pierce/td:nth-of-type(2) > input'
            ],
            [
                'text/同意する'
            ]
        ],
        offsetY: 18.6875,
        offsetX: 47.125,
        assertedEvents: [
            {
                type: 'navigation',
                url: 'https://www.vo3is-vso.mcdb.ricoh.com/dummy.html?SUAV5nxRniv0/wPE1u0KWw==&SUAV5nxRniv0/wPE1u0KWw==&p000h12834&kgdNG7cS4tQufCgOvKr1RQ==&kgdNG7cS4tQufCgOvKr1RQ==&01634563&null&KSKOvReIWYYfm2RBu5HtBQ==&g10012013&null&SUAV5nxRniv0/wPE1u0KWw==&kgdNG7cS4tQufCgOvKr1RQ==&8klQB3w5k2RDCNM2h65NDw==&&&https://www.vo3is.ricoh.co.jp/portal/portalMain.do',
                title: ''
            }
        ]
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'click',
        target: 'main',
        selectors: [
            [
                '#menu1menu1_10 tr:nth-of-type(1) div'
            ],
            [
                'xpath///*[@id="_menu1menu1_10_1"]/div'
            ],
            [
                'pierce/#menu1menu1_10 tr:nth-of-type(1) div'
            ]
        ],
        offsetY: 8.5,
        offsetX: 63,
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'main',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyUp',
        key: 'Control',
        target: 'main'
    });
    await runner.runStep({
        type: 'click',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA0000M.do',
        selectors: [
            [
                'table:nth-of-type(3) input:nth-of-type(3)'
            ],
            [
                'xpath///*[@id="L1_PagerNextPage"]'
            ],
            [
                'pierce/table:nth-of-type(3) input:nth-of-type(3)'
            ]
        ],
        offsetY: 6.392059326171875,
        offsetX: 15.5511474609375,
        assertedEvents: [
            {
                type: 'navigation',
                url: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/PagerNextPage.do?pageId=sjfxxaa3xForm&pagerId=L1',
                title: ''
            }
        ]
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/PagerNextPage.do?pageId=sjfxxaa3xForm&pagerId=L1',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/PagerNextPage.do?pageId=sjfxxaa3xForm&pagerId=L1',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/PagerNextPage.do?pageId=sjfxxaa3xForm&pagerId=L1',
        key: 'Control'
    });
    await runner.runStep({
        type: 'click',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/PagerNextPage.do?pageId=sjfxxaa3xForm&pagerId=L1',
        selectors: [
            [
                'tbody:nth-of-type(6) input'
            ],
            [
                'xpath///*[@id="SJFXXAA3X01M"]'
            ],
            [
                'pierce/tbody:nth-of-type(6) input'
            ]
        ],
        offsetY: 11.545455932617188,
        offsetX: 33.81818389892578,
        assertedEvents: [
            {
                type: 'navigation',
                url: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
                title: ''
            }
        ]
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/PagerNextPage.do?pageId=sjfxxaa3xForm&pagerId=L1',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/PagerNextPage.do?pageId=sjfxxaa3xForm&pagerId=L1',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyUp',
        key: 'Control',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'click',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        selectors: [
            [
                'aria/受注共通照会[role="link"]',
                'aria/[role="generic"]'
            ],
            [
                '#DISPLAYED_TITLE\\[6\\]'
            ],
            [
                'xpath///*[@id="DISPLAYED_TITLE[6]"]'
            ],
            [
                'pierce/#DISPLAYED_TITLE\\[6\\]'
            ],
            [
                'text/受注共通照会'
            ]
        ],
        offsetY: 9.017059326171875,
        offsetX: 50.369319915771484,
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyUp',
        key: 'Control',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jf_menu-jpi/SJFXXAA3X01M.do?ID=15'
    });
    await runner.runStep({
        type: 'click',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jfax-jpi/menu.do',
        selectors: [
            [
                '#INQUIRY_NUM'
            ],
            [
                'xpath///*[@id="INQUIRY_NUM"]'
            ],
            [
                'pierce/#INQUIRY_NUM'
            ]
        ],
        offsetY: 8.000007629394531,
        offsetX: 70.84660339355469,
    });
    await runner.runStep({
        type: 'change',
        value: 'JS389353684',
        selectors: [
            [
                '#INQUIRY_NUM'
            ],
            [
                'xpath///*[@id="INQUIRY_NUM"]'
            ],
            [
                'pierce/#INQUIRY_NUM'
            ]
        ],
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jfax-jpi/menu.do'
    });
    await runner.runStep({
        type: 'click',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jfax-jpi/menu.do',
        selectors: [
            [
                'aria/管理番号検索[role="button"]'
            ],
            [
                '#SJFAARC1S02P'
            ],
            [
                'xpath///*[@id="SJFAARC1S02P"]'
            ],
            [
                'pierce/#SJFAARC1S02P'
            ]
        ],
        offsetY: 5.5397796630859375,
        offsetX: 37.42901611328125,
        assertedEvents: [
            {
                type: 'navigation',
                url: 'https://www.jx1.nihon-os.ricoh.co.jp/jfax-jpi/SJFAARC1S02P.do',
                title: ''
            }
        ]
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jfax-jpi/SJFAARC1S02P.do',
        key: 'Control'
    });
    await runner.runStep({
        type: 'click',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jfax-jpi/SJFAARC1S02P.do',
        selectors: [
            [
                'aria/照会[role="button"]'
            ],
            [
                '#SJFAARC2L01P\\[0\\]'
            ],
            [
                'xpath///*[@id="SJFAARC2L01P[0]"]'
            ],
            [
                'pierce/#SJFAARC2L01P\\[0\\]'
            ]
        ],
        offsetY: 9.71307373046875,
        offsetX: 25.965911865234375,
    });
    await runner.runStep({
        type: 'keyDown',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jfax-jpi/SJFAARC1S02P.do',
        key: 'Control'
    });
    await runner.runStep({
        type: 'keyUp',
        key: 'Control',
        target: 'https://www.jx1.nihon-os.ricoh.co.jp/jfax-jpi/SJFAARC1S02P.do'
    });

    await runner.runAfterAllSteps();
}

if (process && import.meta.url === url.pathToFileURL(process.argv[1]).href) {
    run()
}
