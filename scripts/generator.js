const fs = require('fs');

const data = `const characters = [
  // HỆ KIM
  {
    id:'tldao', name:'Thiếu Lâm', branch:'Đao Pháp', role:'Ngoại Công Cơ Động', element:'Kim',
    emoji:'🗡️', color:'#e67e22', colorGlow:'rgba(230,126,34,0.3)',
    description:'Đánh trên ngựa, tốc độ đánh cao, sức chịu đựng tốt. Khắc tinh của sinh lực yếu.',
    baseStats:{sm:30,tp:15,sk:25,nl:10},
    buildGuide:{
      summary:'Sức Mạnh tăng sát thương, Sinh Khí đảm bảo sinh tồn.',
      phases:[
        {level:'1-60',sm:'Đủ mặc đồ',tp:'0',sk:'Còn lại',nl:'0',note:'Dùng Bổng để train nhanh trước cấp 60'},
        {level:'60-90',sm:'Mốc 200-250',tp:'0',sk:'Dồn hết',nl:'0',note:'Chuyển qua Đao, cần SK cao để tank'},
        {level:'90-150',sm:'Mốc 260',tp:'Mốc 150',sk:'Còn lại',nl:'0',note:'TP đủ để không miss, SK cực lớn end game'}
      ],
      calc:{smTarget:260,smReachAt:90,tpRate:[{f:90,t:150,p:1}],nlFixed:0}
    },
    skills:[
      {name:'Bất Động Minh Vương',type:'Buff',priority:1,desc:'Sinh Tồn',level:'1x'},
      {name:'Vô Tướng Trảm',type:'DPS',priority:2,desc:'Kỹ năng 9x trên ngựa',level:'9x'},
      {name:'La Hán Trận',type:'Counter',priority:3,desc:'Phản đòn',level:'3x'}
    ],
    equipment:[{stat:'Kháng Tất Cả',importance:'⭐⭐⭐⭐⭐',note:'Thiết yếu'},{stat:'Tốc đánh',importance:'⭐⭐⭐⭐',note:'Đánh đao cần tốc'}]
  },
  {
    id:'tlbong', name:'Thiếu Lâm', branch:'Bổng Pháp', role:'Tank / Gom Quái', element:'Kim',
    emoji:'🛡️', color:'#e67e22', colorGlow:'rgba(230,126,34,0.3)',
    description:'AoE gom quái siêu hạng, phản đòn mạnh mẽ.',
    baseStats:{sm:30,tp:15,sk:25,nl:10},
    buildGuide:{
      summary:'Sinh Khí là vua. Bất tử giữa bầy quái.',
      phases:[
        {level:'1-90',sm:'200',tp:'0',sk:'Dồn hết',nl:'0',note:'Đủ SM lực tay gom quái'},
        {level:'90-150',sm:'260',tp:'50',sk:'Dồn hết',nl:'0',note:'Tăng thêm SM mặc đồ xanh'}
      ],
      calc:{smTarget:260,smReachAt:90,tpRate:[{f:90,t:150,p:1}],nlFixed:0}
    },
    skills:[
      {name:'Hoành Tảo Thiên Quân',type:'AoE',priority:1,desc:'Choáng diện rộng',level:'9x'},
      {name:'Dịch Cân Kinh',type:'Buff',priority:2,desc:'Max kháng',level:'3x'}
    ],
    equipment:[{stat:'Sinh lực',importance:'⭐⭐⭐⭐⭐',note:'Càng trâu càng tốt'},{stat:'Phản đòn',importance:'⭐⭐⭐⭐',note:'La hán + đồ phản'}]
  },
  {
    id:'tvchuy', name:'Thiên Vương', branch:'Chùy Pháp', role:'Sốc Sát Thương', element:'Kim',
    emoji:'🔨', color:'#d35400', colorGlow:'rgba(211,84,0,0.3)',
    description:'Lực tay to nhất game, khả năng xuất chiêu 1 đập chết luôn đối thủ yếu máu.',
    baseStats:{sm:30,tp:10,sk:30,nl:10},
    buildGuide:{
      summary:'Sức Mạnh quyết định tất cả. Một đập bay màu.',
      phases:[
        {level:'1-90',sm:'Dồn hết',tp:'0',sk:'1đ/lv',nl:'0',note:'Gây dame cực to'},
        {level:'90-150',sm:'Dồn hết',tp:'50',sk:'Mốc 150',nl:'0',note:'SK đủ không bị đột tử'}
      ],
      calc:{smTarget:300,smReachAt:60,tpRate:[{f:90,t:150,p:1}],nlFixed:0} // Simplified mock
    },
    skills:[
      {name:'Chùy Tôn',type:'Hỗ trợ',priority:1,desc:'Tăng sát thương chùy',level:'1x'},
      {name:'Truy Tinh Trục Nguyệt',type:'DPS',priority:2,desc:'Kỹ năng 9x cực đỉnh',level:'9x'}
    ],
    equipment:[{stat:'Sát thương vật lý',importance:'⭐⭐⭐⭐⭐',note:'Max damage'},{stat:'Tốc đánh',importance:'⭐⭐⭐⭐',note:'Mốc 94%'}]
  },
  {
    id:'tvthuong', name:'Thiên Vương', branch:'Thương Pháp', role:'Đâm Liên Hoàn', element:'Kim',
    emoji:'🔱', color:'#d35400', colorGlow:'rgba(211,84,0,0.3)',
    description:'Tốc độ đánh nhanh nhất game, dồn hiệu ứng liên tục khiến mục tiêu bất động.',
    baseStats:{sm:30,tp:10,sk:30,nl:10},
    buildGuide:{
      summary:'Cân bằng SM và SK, lấy tốc độ bù lực tay.',
      phases:[
        {level:'1-90',sm:'250',tp:'0',sk:'Còn lại',nl:'0',note:'Thương dame nhỏ nên cần sống lâu đâm nhiều'},
        {level:'90-150',sm:'300',tp:'0',sk:'Dồn hết',nl:'0',note:'Huyết Chiến Bát Phương cần trâu bò'}
      ],
      calc:{smTarget:250,smReachAt:80,tpRate:[{f:1,t:150,p:0}],nlFixed:0}
    },
    skills:[
      {name:'Huyết Chiến Bát Phương',type:'Cận Chiến',priority:1,desc:'9x Thọc liên tục',level:'9x'},
      {name:'Kim Chung Tráo',type:'Kháng',priority:2,desc:'Tăng mọi loại kháng',level:'1x'}
    ],
    equipment:[{stat:'Tốc đánh',importance:'⭐⭐⭐⭐⭐',note:'Bắt buộc mốc cao nhất'},{stat:'Băng sát',importance:'⭐⭐⭐⭐',note:'Đâm liên tục + làm chậm = bá đạo'}]
  },

  // HỆ MỘC
  {
    id:'dmno', name:'Đường Môn', branch:'Nỏ Tiễn', role:'AoE DPS', element:'Mộc',
    emoji:'🎯', color:'#2ecc71', colorGlow:'rgba(46,204,113,0.3)',
    description:'Sát thương AoE tầm xa cực mạnh. Bạo Vũ Lê Hoa, Thiên La Vạn Tiễn dọn quái.',
    baseStats:{sm:20,tp:30,sk:20,nl:10},
    buildGuide:{
      summary:'Thân Pháp là vua. SM đủ mặc đồ đồ.',
      phases:[
        {level:'1-90',sm:'165',tp:'Dồn hết',sk:'Còn lại',nl:'0',note:'Thân pháp tạo sát thương ngoại cho tiễn'},
        {level:'90-150',sm:'165',tp:'Dồn hết',sk:'Tối thiểu',nl:'0',note:'Giữ SM, dồn hết hỏa lực vào TP'}
      ],
      calc:{smTarget:165,smReachAt:60,tpRate:[{f:1,t:150,p:3}],nlFixed:0}
    },
    skills:[
      {name:'Thiên La Vạn Tiễn',type:'AoE',priority:1,desc:'Skill 9x nuke',level:'9x'},
      {name:'Đường Môn Ám Khí',type:'Nội tại',priority:2,desc:'Tăng damage',level:'1x'}
    ],
    equipment:[{stat:'Hút Nội Lực',importance:'⭐⭐⭐⭐⭐',note:'NL bằng 0 nên phải hút'},{stat:'Tốc đánh',importance:'⭐⭐⭐⭐',note:'Bắn nhanh = sát thương'}]
  },
  {
    id:'dmtieu', name:'Đường Môn', branch:'Phi Tiêu', role:'Hit & Run', element:'Mộc',
    emoji:'🔪', color:'#2ecc71', colorGlow:'rgba(46,204,113,0.3)',
    description:'Cơ động cực cao trên ngựa, Phi tiêu nảy giữa nhiều mục tiêu.',
    baseStats:{sm:20,tp:30,sk:20,nl:10},
    buildGuide:{
      summary:'Tăng theo Thân Pháp. Đạt đỉnh cao thả diều bắt lẻ.',
      phases:[
        {level:'1-90',sm:'165',tp:'Dồn hết',sk:'Còn lại',nl:'0',note:'Giống Đường Môn Nỏ'},
        {level:'90-150',sm:'165',tp:'Dồn hết',sk:'Tối thiểu',nl:'0',note:'Đoạn Mộc Phệ Tâm nảy rất đau'}
      ],
      calc:{smTarget:165,smReachAt:60,tpRate:[{f:1,t:150,p:3}],nlFixed:0}
    },
    skills:[
      {name:'Nhiếp Hồn Nguyệt Ảnh',type:'Phi tiêu',priority:1,desc:'Skill 9x nảy nhiều mục tiêu',level:'9x'},
      {name:'Mãn Thiên Hoa Vũ',type:'AoE nhỏ',priority:2,desc:'Skill cơ bản',level:'5x'}
    ],
    equipment:[{stat:'Thời gian phục hồi',importance:'⭐⭐⭐⭐⭐',note:'Phải có trên ngựa'},{stat:'Băng Sát Ngoại',importance:'⭐⭐⭐⭐',note:'Thả diều không cho đối thủ tới gần'}]
  },
  {
    id:'dndchuong', name:'Ngũ Độc', branch:'Chưởng Độc', role:'Sát Thương Nội', element:'Mộc',
    emoji:'☠️', color:'#1abc9c', colorGlow:'rgba(26,188,156,0.3)',
    description:'Không cần nội ngoại công, sát thương phụ thuộc % Độc Sát. Rất trâu bò.',
    baseStats:{sm:20,tp:15,sk:25,nl:20},
    buildGuide:{
      summary:'Toàn bộ vào Sinh Khí. Độc không phụ thuộc thuộc tính.',
      phases:[
        {level:'1-90',sm:'Đủ mặc đồ',tp:'0',sk:'Dồn hết',nl:'0',note:'Skill rất ít tốn NL, SK làm tanker thả bùa'},
        {level:'90-150',sm:'Mốc 165',tp:'0',sk:'Dồn hết',nl:'0',note:'Âm Phong Thực Cốt bào máu quá tốt.'}
      ],
      calc:{smTarget:165,smReachAt:60,tpRate:[{f:1,t:150,p:0}],nlFixed:0}
    },
    skills:[
      {name:'Âm Phong Thực Cốt',type:'AoE Nội',priority:1,desc:'Skill 9x phá đội hình',level:'9x'},
      {name:'Vạn Cổ Thực Tâm',type:'Bùa',priority:2,desc:'Giảm kháng mộc',level:'5x'}
    ],
    equipment:[{stat:'Kỹ năng môn phái +1/2',importance:'⭐⭐⭐⭐⭐',note:'Skill level cực kỳ quan trọng cho Độc Sát'},{stat:'Kháng Kim',importance:'⭐⭐⭐⭐',note:'Đỡ bị Thiên Vương đập chết'}]
  },

  // HỆ THỦY
  {
    id:'nmbuff', name:'Nga My', branch:'Support', role:'Healer Tối Thượng', element:'Thủy',
    emoji:'💚', color:'#3498db', colorGlow:'rgba(52,152,219,0.3)',
    description:'Trụ cột không thể thiếu của mọi loại Party. Cung cấp máu và kháng tính.',
    baseStats:{sm:15,tp:20,sk:20,nl:25},
    buildGuide:{
      summary:'Trâu nhất có thể. Nga My sống thì Party sống.',
      phases:[
        {level:'1-90',sm:'Đủ mặc đồ áo',tp:'0',sk:'Dồn hết',nl:'Vừa đủ',note:'HP là ưu tiên tiên quyết'},
        {level:'90-150',sm:'250',tp:'0',sk:'Dồn hết',nl:'Vừa đủ',note:'Tẩy tủy lấy base máu to tối đa'}
      ],
      calc:{smTarget:250,smReachAt:60,tpRate:[{f:1,t:150,p:0}],nlFixed:50}
    },
    skills:[
      {name:'Từ Hàng Phổ Độ',type:'Buff',priority:1,desc:'Hồi lượng máu khổng lồ',level:'5x'},
      {name:'Mộng Điệp',type:'Buff',priority:2,desc:'Hồi SL/NL tự động',level:'3x'}
    ],
    equipment:[{stat:'Sinh Lực',importance:'⭐⭐⭐⭐⭐',note:'Mấu chốt sinh tồn'},{stat:'Tốc độ hồi SL',importance:'⭐⭐⭐⭐',note:'Sống dai'}]
  },
  {
    id:'tydao', name:'Thúy Yên', branch:'Đao Pháp', role:'Sát Thủ Tàng Hình', element:'Thủy',
    emoji:'🥷', color:'#2980b9', colorGlow:'rgba(41,128,185,0.3)',
    description:'Ẩn mình và tung ra nhát chém kinh hoàng tước đoạt mạng sống kẻ địch ít máu.',
    baseStats:{sm:20,tp:25,sk:15,nl:20},
    buildGuide:{
      summary:'Tốc độ và Cớ động. Băng sát cực rát.',
      phases:[
        {level:'1-90',sm:'210',tp:'Dồn hết',sk:'Tối thiểu',nl:'0',note:'Chủ yếu đi PK tàng hình'},
        {level:'90-150',sm:'260',tp:'Dồn hết',sk:'Vừa đủ',nl:'0',note:'Skill 9x xả combo cực rát'}
      ],
      calc:{smTarget:260,smReachAt:90,tpRate:[{f:1,t:150,p:3}],nlFixed:0}
    },
    skills:[
      {name:'Băng Tung Vô Ảnh',type:'Đột kích',priority:1,desc:'Sát thương dồn 9x',level:'9x'},
      {name:'Tàng Hình',type:'Nội tại',priority:2,desc:'Che giấu bản thân',level:'3x'}
    ],
    equipment:[{stat:'Băng Sát',importance:'⭐⭐⭐⭐⭐',note:'Phối hợp chiêu phái'},{stat:'Tốc độ chạy',importance:'⭐⭐⭐⭐',note:'Tàng hình áp sát'}]
  },

  // HỆ HỎA
  {
    id:'cbchuong', name:'Cái Bang', branch:'Chưởng Pháp', role:'Nội Công Nuke', element:'Hỏa',
    emoji:'🐉', color:'#e74c3c', colorGlow:'rgba(231,76,60,0.3)',
    description:'Thả rồng săn đuổi mục tiêu (Kháng Long Hữu Hồi), lượng Nội Lực quyết định độ mạnh.',
    baseStats:{sm:20,tp:15,sk:20,nl:25},
    buildGuide:{
      summary:'Hệ Nội Công nhưng không tăng nội lực! Dồn toàn bộ Sinh Khí.',
      phases:[
        {level:'1-90',sm:'Mốc áo',tp:'0',sk:'Dồn hết',nl:'0',note:'Chưởng CB tốn rất nhiều Mana, nhưng có skill hồi'},
        {level:'90-150',sm:'165',tp:'0',sk:'Dồn hết',nl:'0',note:'Phi Long Tại Thiên rượt đuổi mục tiêu'}
      ],
      calc:{smTarget:165,smReachAt:60,tpRate:[{f:1,t:150,p:0}],nlFixed:0}
    },
    skills:[
      {name:'Phi Long Tại Thiên',type:'Dấu vết rồng',priority:1,desc:'Rượt mục tiêu',level:'9x'},
      {name:'Thâu Long Chuyển Phượng',type:'Hồi Mana',priority:2,desc:'Biến máu thành mana',level:'3x'}
    ],
    equipment:[{stat:'Kháng Thủy',importance:'⭐⭐⭐⭐⭐',note:'Đỡ bị Nga My/Thúy Yên đè'},{stat:'Tốc độ xuất chiêu',importance:'⭐⭐⭐⭐',note:'Thả rồng liên tục'}]
  },
  {
    id:'tnthuong', name:'Thiên Nhẫn', branch:'Thương Pháp', role:'Nội Công Hỏa', element:'Hỏa',
    emoji:'🔥', color:'#c0392b', colorGlow:'rgba(192,57,43,0.3)',
    description:'Thiên Ngoại Lưu Tinh gây sát thương lửa nội, kèm hệ thống bùa chú cực lợi hại.',
    baseStats:{sm:25,tp:15,sk:20,nl:20},
    buildGuide:{
      summary:'Nội Lực và Sinh Khí song hành. Farm bãi quái cực lẹ.',
      phases:[
        {level:'1-90',sm:'Mốc Áo',tp:'0',sk:'1đ/lv',nl:'Dồn hết',note:'Skill tốn mana nhiều. Nương nhờ Nội Lực.'},
        {level:'90-150',sm:'165',tp:'0',sk:'Cân đối',nl:'Dồn hết',note:'Vân Long Kích diện rộng'}
      ],
      calc:{smTarget:165,smReachAt:60,tpRate:[{f:1,t:150,p:0}],nlFixed:150} // mock
    },
    skills:[
      {name:'Vân Long Kích',type:'Nội Công',priority:1,desc:'AoE hỏa sát',level:'9x'},
      {name:'Phiến Đã Liêu Nguyên',type:'Bùa Hỏa',priority:2,desc:'Trừ kháng hỏa',level:'5x'}
    ],
    equipment:[{stat:'Kỹ Năng Phái +',importance:'⭐⭐⭐⭐⭐',note:'Dành cho Bùa chú / Chiêu'},{stat:'Tốc đánh',importance:'⭐⭐⭐⭐',note:'Xuất chiêu nhanh'}]
  },

  // HỆ THỔ
  {
    id:'vdkhik', name:'Võ Đang', branch:'Khí Tông', role:'Control Nội Công', element:'Thổ',
    emoji:'🌀', color:'#9b59b6', colorGlow:'rgba(155,89,182,0.3)',
    description:'Gây choáng cực khó chịu. Dùng khiên Tọa Vọng bù đắp Sinh Khí yếu.',
    baseStats:{sm:15,tp:20,sk:20,nl:25},
    buildGuide:{
      summary:'Nội lực là Sát thương và là Máu.',
      phases:[
        {level:'1-90',sm:'110',tp:'0',sk:'0',nl:'Dồn hết',note:'Tọa Vọng Vô Ngã hút sát thương bằng Nội Lực'},
        {level:'90-150',sm:'110',tp:'0',sk:'0',nl:'Dồn hết',note:'Skill 9x Bác Cấp Nhi Phục cần Nội lực siêu cao'}
      ],
      calc:{smTarget:110,smReachAt:40,tpRate:[{f:1,t:150,p:0}],nlFixed:-1} // all remaining to nl
    },
    skills:[
      {name:'Bác Cấp Nhi Phục',type:'Sét Nội AoE',priority:1,desc:'Choáng giật liên hoàn',level:'9x'},
      {name:'Tọa Vọng Vô Ngã',type:'Khiên Nội',priority:2,desc:'Cốt lõi sinh tồn',level:'1x'}
    ],
    equipment:[{stat:'Chuyển sát thương thành Nội lực',importance:'⭐⭐⭐⭐⭐',note:'Quyết định độ trâu'},{stat:'Hút Nội',importance:'⭐⭐⭐⭐',note:'Bơm lại mana'}]
  },
  {
    id:'clkiem', name:'Côn Lôn', branch:'Kiếm Pháp', role:'Pháp Sư Sét', element:'Thổ',
    emoji:'⚡', color:'#8e44ad', colorGlow:'rgba(142,68,173,0.3)',
    description:'Thiên Lôi Chấn Địa gây giật choáng đỉnh cao. Nội công cực mạnh.',
    baseStats:{sm:20,tp:25,sk:15,nl:20},
    buildGuide:{
      summary:'Giật lôi liên hồi. Yếu cầu Nội Lực & Sinh Khí tốt.',
      phases:[
        {level:'1-90',sm:'110',tp:'0',sk:'1đ/lv',nl:'Dồn hết',note:'Dame rất bạo'},
        {level:'90-150',sm:'165',tp:'0',sk:'Cân đối',nl:'Dồn hết',note:'Lôi Động Cửu Thiên giật phát chết luôn'}
      ],
      calc:{smTarget:165,smReachAt:60,tpRate:[{f:1,t:150,p:0}],nlFixed:150}
    },
    skills:[
      {name:'Lôi Động Cửu Thiên',type:'Choáng Đỉnh',priority:1,desc:'Choáng siêu dài',level:'9x'},
      {name:'Thanh Phong Phù',type:'Chạy Nhanh',priority:2,desc:'1 trong tựa buff cơ động',level:'3x'}
    ],
    equipment:[{stat:'Nội lực',importance:'⭐⭐⭐⭐⭐',note:'Côn lôn tốn mana vô cùng'},{stat:'Tốc xuất chiêu',importance:'⭐⭐⭐⭐',note:'Giật lôi không delay'}]
  }
];

const cssFilters = \`
.filters { display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; margin-bottom: 32px; }
.filter-btn { padding: 6px 16px; border-radius: 20px; border: 1px solid var(--border-subtle); background: var(--bg-secondary); color: var(--text-secondary); cursor: pointer; transition: 0.2s; font-weight: 500; font-size: 14px; }
.filter-btn:hover { background: var(--bg-glass); border-color: var(--text-muted); }
.filter-btn.active { background: var(--gold-dim); border-color: var(--gold); color: var(--gold) !important; }
.fav-btn { position: absolute; top: 16px; right: 16px; background: rgba(0,0,0,0.5); border: 1px solid var(--border-subtle); border-radius: 50%; width: 32px; height: 32px; font-size: 14px; cursor: pointer; transition: 0.2s; display: flex; align-items: center; justify-content: center; z-index: 2; opacity: 0.5; }
.fav-btn.active { opacity: 1; border-color: var(--crimson); text-shadow: 0 0 10px red; }
.fav-btn:hover { opacity: 1; transform: scale(1.1); }
\`;

function processHtml() {
  let html = fs.readFileSync('index.html', 'utf-8');
  
  // 1: Replace characters definition
  const startChars = html.indexOf('const characters = [');
  const endChars = html.indexOf('];', startChars) + 2;
  html = html.substring(0, startChars) + data + html.substring(endChars);

  // 2: Inject CSS
  if (!html.includes('.filters {')) {
    html = html.replace('</style>', cssFilters + '\\n</style>');
  }

  // 3: Replace renderTeam logic to include Filters and Favs
  const oldRenderTeamStr = html.substring(html.indexOf('function renderTeam() {'), html.indexOf('function renderChar', html.indexOf('function renderTeam() {')));
  const newRenderTeam = \`function renderTeam() {
  const fil = currentParam || 'all';
  let filtered = characters;
  const favs = JSON.parse(localStorage.getItem('vltk_favs')||'[]');
  if(fil === 'fav') {
    filtered = characters.filter(c => favs.includes(c.id));
  } else if(fil !== 'all') {
    filtered = characters.filter(c => c.element === fil);
  }
  
  return \\\`<div class="page-header"><h1 class="page-title">Cẩm Nang 10 Phái VLTK1</h1>
    <p class="page-subtitle">Tuyển tập Cách nâng điểm & Phối đồ 13 hệ phái kinh điển nhất</p>
    <div class="filters" style="margin-top:24px">
      <button class="filter-btn \\\${fil==='all'?'active':''}" onclick="go('team','all')">Tất cả</button>
      <button class="filter-btn \\\${fil==='fav'?'active':''}" onclick="go('team','fav')">❤️ Yêu Thích</button>
      <button class="filter-btn \\\${fil==='Kim'?'active':''}" style="color:var(--orange)" onclick="go('team','Kim')">⚔️ Kim</button>
      <button class="filter-btn \\\${fil==='Mộc'?'active':''}" style="color:var(--green)" onclick="go('team','Mộc')">🌿 Mộc</button>
      <button class="filter-btn \\\${fil==='Thủy'?'active':''}" style="color:var(--blue)" onclick="go('team','Thủy')">💧 Thủy</button>
      <button class="filter-btn \\\${fil==='Hỏa'?'active':''}" style="color:var(--crimson)" onclick="go('team','Hỏa')">🔥 Hỏa</button>
      <button class="filter-btn \\\${fil==='Thổ'?'active':''}" style="color:var(--purple)" onclick="go('team','Thổ')">🪨 Thổ</button>
    </div></div>
    <div class="team-grid">\\\${filtered.length ? filtered.map(c => \\\`
      <div class="char-card" onclick="go('char','\\\${c.id}')" style="--card-color:\\\${c.color};--card-glow:\\\${c.colorGlow}">
        <button class="fav-btn \\\${favs.includes(c.id)?'active':''}" onclick="event.stopPropagation();toggleFav('\\\${c.id}')">❤️</button>
        <div class="char-card-header"><div class="char-emoji">\\\${c.emoji}</div>
          <div class="char-info"><h3>\\\${c.name}</h3><span class="char-branch">\\\${c.branch}</span></div></div>
        <span class="char-role" style="background:\\\${c.colorGlow};color:\\\${c.color}">\\\${c.role}</span>
        <p class="char-desc">\\\${c.description}</p>
        <div class="char-card-footer"><span class="char-element">Hệ \\\${c.element}</span>
          <span class="char-view-btn">Xem chi tiết →</span></div>
      </div>\\\`).join('') : '<p style="grid-column:1/-1;text-align:center;color:var(--text-muted)">Chưa có phái nào trong danh sách này!</p>'}</div>\\\`;
}
\`;
  html = html.replace(oldRenderTeamStr, newRenderTeam);
  
  // 4: Add toggleFav
  if(!html.includes('function toggleFav')) {
    html = html.replace('function switchTab', \`function toggleFav(id) {
  let favs = JSON.parse(localStorage.getItem('vltk_favs')||'[]');
  if(favs.includes(id)) favs = favs.filter(x => x!==id);
  else favs.push(id);
  localStorage.setItem('vltk_favs', JSON.stringify(favs));
  if(currentPage === 'team') render();
}

function switchTab\`);
  }

  // 5: Update Nav links properly
  html = html.replace('<a class="nav-link active" data-page="team" onclick="go(\\'team\\')"><span>👥</span><span>Đội Hình</span></a>',
                      '<a class="nav-link active" data-page="team" onclick="go(\\'team\\', \\'all\\')"><span>📚</span><span>Các Phái</span></a>');
                      
  // Write
  fs.writeFileSync('index.html', html, 'utf-8');
  console.log('Update Success!');
}
processHtml();
