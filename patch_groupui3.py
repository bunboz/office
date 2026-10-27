# -*- coding: utf-8 -*-
# Chỉnh "Quản lý nhóm đề xuất" gọn và đẹp hơn: một block CSS phủ cuối + sort đúng cột.
p = '/Users/test/Documents/OFFICE/base-easy/index.html'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:80]
    s = s.replace(a, b, 1)

# sort: xóa biến chết us/dm/pn, thêm 'st'
rep("  const key={name:g=>(g.name||'').toLowerCase(),sla:g=>g.sla||0,pend:pend,st:g=>g.active?1:0}[so.k];",
    "  const key={name:g=>(g.name||'').toLowerCase(),sla:g=>g.sla||0,pend:pend,gactive:g=>g.active?1:0}[so.k];")
rep("${hd('st','TRẠNG THÁI')}", "${hd('gactive','TRẠNG THÁI')}")
rep("const st=g.draft?'dr':g.active?'on':'off', us=[...new Set(g.blocks.flatMap(bk=>bk.t==='direct'?[]:(bk.u||[])))], dm=g.blocks.some(bk=>bk.t==='direct'), pn=pend(g);",
    "const st=g.draft?'dr':g.active?'on':'off';")
rep(").join(''):'')+'</div>'", ").join(''):'<div class=\"gbempty\">Chưa có nhóm nào trong thư mục này.</div>')}</div>'")

css = '''
/* ===== màn Quản lý nhóm đề xuất: tinh chỉnh lần 3 ===== */
.gbhead{padding:14px 24px 2px;background:#fff;}
.gbhead .mhead{border:none;background:none;padding:0;align-items:center;}
.gbhead .mhead .row{width:100%;gap:14px;}
.gbhead h1{font-size:18px;line-height:24px;margin:0 0 10px;font-weight:700;letter-spacing:-.2px;}
.gbhead .tab{padding:10px 12px;font-size:13px;font-weight:600;}
.gbhead .tab .tcn{min-width:20px;text-align:center;}
.gbhead #gsq{height:34px;border-radius:var(--r-xs);border-color:var(--n-400);width:200px;justify-self:end;}
/* khung thư mục: phẳng, góc bo nhỏ, không bóng */
.gbx{background:#fff;border:1px solid var(--n-300);border-radius:var(--r-xs);margin-bottom:14px;box-shadow:none;overflow:visible;}
.gbh{padding:13px 18px;gap:10px;}
.gbfic{color:var(--primary-500);display:inline-flex;}
.gbfic svg{fill:none;stroke:currentColor;stroke-width:1.8;width:16px;height:16px;}
.gbh b{font-size:15px;font-weight:700;letter-spacing:-.1px;}
.gbh small{font-size:12px;color:var(--n-700);margin-left:2px;}
.gcr{margin-left:auto;}
/* hàng tiêu đề: nền xám rất nhạt, chữ mảnh, không in hoa to */
.gth{background:#f7f9f9;border-bottom:1px solid var(--n-300);border-top:1px solid var(--n-300);min-height:34px;}
.gth .gsb,.gth .gth-q,.gth .gth-star{color:var(--n-700);text-transform:none;letter-spacing:0;font-weight:500;}
.gth .gsb:hover,.gth .gsb.on{color:var(--n-900);}
/* các dòng: cao hơn, căn đều, hover rõ */
.gr2{min-height:60px;padding:12px 18px;border-bottom:1px solid #eceeee;}
.gr2:last-child{border-bottom:none;}
.gr2:hover{background:#f6fafa;}
.gr2.off{background:#fafbfb;} .gr2.dr{background:#fffdf5;}
.gr2.off .g2n b,.gr2.off .g2n span,.gr2.off .g2f,.gr2.off .g2s{color:var(--n-700);}
.gr2 .star svg{fill:none;stroke:currentColor;stroke-width:1.8;width:18px;height:18px;}
.gr2 .star.on svg{fill:#fec84b;stroke:#fec84b;}
.g2n b{font-size:14px;font-weight:600;}
.g2n span{margin-top:2px;}
/* nút Sửa: luôn thấy, nhỏ, chữ đơn; nút nhân bản mới là hover */
.gr2 .g2b .btn{padding:0 10px;height:30px;font-size:13px;justify-self:end;}
.gr2 .g2b .btn.ico{width:30px;height:30px;opacity:0;}
.gr2:hover .g2b .btn.ico{opacity:1;}
.gr2 .g2b{opacity:1;}
/* trạng thái: switch lớn hơn một chút, chữ kèm theo */
.gr2 .sw{width:34px;height:20px;}
.gr2 .sw::after{width:14px;height:14px;}
.gr2 .sw.on::after{transform:translateX(14px);}
.g2l{font-size:12px;font-weight:600;}
.g2f{font-size:12px;}
/* ô trống trong thư mục */
.gbempty{padding:20px;font-size:13px;color:var(--n-700);text-align:center;background:#fff;}
/* mobile */
@media (max-width:1280px){ .gr2 .star{display:none;} .gth .gth-star{display:none;} }
'''
i = s.rindex('</style>')
s = s[:i] + css + s[i:]
open(p, 'w', encoding='utf-8').write(s)
print('ok')
