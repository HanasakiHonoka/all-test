# encoding: utf-8
import json
from string import Template

def work1():
    raw = '''
stock_detail	前10大股东持股明细（数组）		[{"sharehd_name":"股东名称","sharehd_type":"股东性质","hd_pct":"持股比例(%)"}]
finance_repo_detail	前10大股权融资回购明细（数组）		[{"invest_name":"投资公司名称","hg_financing_amount":"融资金额(元)","repo_year":"回购期限（年）","repo_rate":"约定回购年利率（%）"}]
dividend_to_price	股息率		
dividend_to_ni	现金分红比例		
ee_hd_rate	员工持股比例（%）		
ee_limit_period	员工持股限售期（月）		
famous_pevc	对应知名机构的融资明细（数组）		[{"famous_pevc_name":"知名PEVC名称"}]
all_pevc_detail	所有PEVC入股明细（数组）		[{"pevc_name":"PEVC名","pevc_hd_rate":"PEVC持股比例（%）","pevc_hd_period":"PEVC持股时间（月）"}]
stock_finance_detail	股权融资明细（数组）		[{"financing_round":"融资轮","lcrz_financing_amount":"融资金额（元）"}]


    '''

    name_list = ["tech", "finance", "manage", "equity", "governance", "es"]
    desc_list = ["核心科技", "财务状况", "业务经营", "股权结构", "公司治理", "持续发展"]
    table = raw = raw.strip().split("\n")
    tmp = Template('''${title}(${id}, "${name}", "${desc}"),''')
    total_prefix = "SSEIN_QIPING"
    second_prefix = "equity"
    total_suffix_list = ["score", "indus_avg", "evaluation_time"]
    id = 200
    for i in range(0, len(name_list)):
        for suffix in total_suffix_list:
            title = "_".join([total_prefix, name_list[i], suffix]).upper()
            print(tmp.substitute(title=title, id=id, name="_".join([name_list[i], suffix]), desc=desc_list[i]))
            id = id + 1

    # for line in table:
        # data = line.split('\t')[3]
        # if data == '':
        #     continue
        # data = json.loads(data)
        # for item in data:
        #     for (k, v) in item.items():
        #         name = k
        #         desc = v
        #         title = "_".join([total_prefix, second_prefix, name]).upper()
        #         print(tmp.substitute(title=title, id=id, name=name, desc=desc))



        # name = data[0]
        # desc = data[1]
        # title = "_".join([total_prefix, second_prefix, name]).upper()
        # print(tmp.substitute(title=title, id=id, name=name, desc=desc))
        # for suffix in total_suffix_list:
        #     title = "_".join([total_prefix, name, suffix]).upper()
        #     name1 = "_".join([name, suffix])
        #     print(tmp.substitute(title=title, id=id, name=name1, desc=desc))
        #     id = id + 1


    pass


def work2():
    raw = '''
    basic_data tech
tech_detail tech
industry_research tech_detail
tech_layout tech_detail
rd_rate tech_detail
rd_stability tech_detail
tech_level tech_detail
tech_influence tech_detail
tech_vitality tech_detail
global_layout tech_detail
equity_detail equity
institution_ownership equity_detail
institution_ownership_detail institution_ownership
famous_institution_ownership institution_ownership_detail
pe_financing_scale institution_ownership_detail
firm_confidence equity_detail
firm_confidence_detail firm_confidence
repurchase_agreement firm_confidence_detail
employee_ownership firm_confidence_detail
dividend firm_confidence_detail
equity_concentration equity_detail
equity_concentration_detail equity_concentration
top_shareholder_ownership equity_concentration_detail
manager_layer_ownership equity_concentration_detail
other_shareholder_ownership equity_concentration_detail
basic_data finance
finance_detail finance
profitability finance_detail
profitability_detail profitability
capital_return profitability_detail
operating_return profitability_detail
growth_ability finance_detail
growth_ability_detail growth_ability
scale_growth growth_ability_detail
income_growth growth_ability_detail
financial_risk finance_detail
financial_risk_detail financial_risk
operating_risk financial_risk_detail
capital_risk financial_risk_detail
capital_structure finance_detail
capital_structure_detail capital_structure
asset_structure capital_structure_detail
debt_structure capital_structure_detail
basic_data es
es_detail es
environment es_detail
environment_detail environment
enmgmt environment_detail
waste environment_detail
enopportnty environment_detail
enrisk environment_detail
resource environment_detail
endispute environment_detail
society es_detail
society_detail society
socialdispute society_detail
pdctliability society_detail
socialopportnty society_detail
healthsafetys society_detail
socialrisk society_detail
supplymgmt society_detail
emdevelopment society_detail
laboright society_detail
manage_detail manage
production_ability manage_detail
production_ability_detail production_ability
production_link production_ability_detail
purchase_link production_ability_detail
sales_ability manage_detail
sales_ability_detail sales_ability
sales_link sales_ability_detail
inventory_link sales_ability_detail
basic_data manage
basic_data governance
governance_detail governance
disclosure governance_detail
corpgovern governance_detail
corpgovern_detail corpgovern
businethics governance_detail
govrndispute governance_detail
riskmgmt governance_detail
    '''

    raw2 = '''
    ee_hd_rate 0.1000000000
ee_limit_period 10
dividend_to_ni 10.0000000000
dividend_to_price 10.0000000000
ee_hd_rate 0.1000000000
ee_limit_period 10
dividend_to_ni 10.0000000000
dividend_to_price 10.0000000000
ee_hd_rate 0.1000000000
ee_limit_period 10
dividend_to_ni 10.0000000000
dividend_to_price 10.0000000000
ee_hd_rate 0.1000000000
ee_limit_period 10
dividend_to_ni 10.0000000000
dividend_to_price 10.0000000000
ee_hd_rate 0.1000000000
ee_limit_period 10
dividend_to_ni 10.0000000000
dividend_to_price 10.0000000000
ee_hd_rate 0.1000000000
ee_limit_period 10
dividend_to_ni 10.0000000000
dividend_to_price 10.0000000000
ee_hd_rate 0.1000000000
ee_limit_period 10
dividend_to_ni 10.0000000000
dividend_to_price 10.0000000000
ee_hd_rate 0.1000000000
ee_limit_period 10
dividend_to_ni 10.0000000000
dividend_to_price 10.0000000000
ee_hd_rate 0.1000000000
ee_limit_period 10
dividend_to_ni 10.0000000000
dividend_to_price 10.0000000000
ee_hd_rate 0.1000000000
ee_limit_period 10
dividend_to_ni 10.0000000000
dividend_to_price 10.0000000000
netprofit_last 100000.000000000000000000
reportdate 2019-12-31
sumasset_last 100000.000000000000000000
sumnonlasset_last 100000.000000000000000000
sumlliab_last 100000.000000000000000000
operatereve_last 100000.000000000000000000
green_education null
infosafety 0E-15
enrisk_score null
enrisk_indus_avg null
socialopportnty_score null
socialopportnty_indus_avg null
socialrisk_score 0.00
socialrisk_indus_avg 70.00
advancereceive 100000.000000000000000000
reportdate 2019-12-31
esg_report 0E-15
indpdirectrto_score 0.02
indpdirectrto_indus_avg 48.17
remaudcmt_score 0.00
remaudcmt_indus_avg 100.00
esgmgmt_indus_avg 0.00
esgmgmt_score 0.00
execuincent_score 0.00
execuincent_indus_avg 90.00
    '''
    table = raw2.strip().split("\n")
    key_set = set()
    tmp = Template('''${title}(${id}, "${name}", "${desc}"),''')
    total_prefix = "SSEIN_QIPING"
    id = 90000
    for line in table:
        key_name = line.split(" ")[0]
        if key_name not in key_set:
            key_set.add(key_name)
            title = "_".join([total_prefix, "mid", key_name]).upper()
            print(tmp.substitute(title=title, id=id, name=key_name, desc=key_name))
            id = id + 1
    # print(table)
    pass


def work4():
    raw = '''
SSEIN_QIPING_TECH_SCORE(200, "tech_score", "核心科技"),
SSEIN_QIPING_TECH_INDUS_AVG(201, "tech_indus_avg", "核心科技"),
SSEIN_QIPING_EVALUATION_TIME(202, "evaluation_time", "evaluation_time"),
SSEIN_QIPING_FINANCE_SCORE(203, "finance_score", "财务状况"),
SSEIN_QIPING_FINANCE_INDUS_AVG(204, "finance_indus_avg", "财务状况"),
SSEIN_QIPING_MANAGE_SCORE(206, "manage_score", "业务经营"),
SSEIN_QIPING_MANAGE_INDUS_AVG(207, "manage_indus_avg", "业务经营"),
SSEIN_QIPING_EQUITY_SCORE(209, "equity_score", "股权结构"),
SSEIN_QIPING_EQUITY_INDUS_AVG(210, "equity_indus_avg", "股权结构"),
SSEIN_QIPING_GOVERNANCE_SCORE(212, "governance_score", "公司治理"),
SSEIN_QIPING_GOVERNANCE_INDUS_AVG(213, "governance_indus_avg", "公司治理"),
SSEIN_QIPING_ES_SCORE(215, "es_score", "持续发展"),
SSEIN_QIPING_ES_INDUS_AVG(216, "es_indus_avg", "持续发展")
    '''

    raw2 = '''
SSEIN_QIPING_TECH_LAYOUT_SCORE(10000, "tech_layout_score", "技术布局"),
SSEIN_QIPING_TECH_LAYOUT_INDUS_AVG(10001, "tech_layout_indus_avg", "技术布局"),
SSEIN_QIPING_TECH_LEVEL_SCORE(10002, "tech_level_score", "技术质量"),
SSEIN_QIPING_TECH_LEVEL_INDUS_AVG(10003, "tech_level_indus_avg", "技术质量"),
SSEIN_QIPING_TECH_INFLUENCE_SCORE(10004, "tech_influence_score", "技术影响力"),
SSEIN_QIPING_TECH_INFLUENCE_INDUS_AVG(10005, "tech_influence_indus_avg", "技术影响力"),
SSEIN_QIPING_TECH_VITALITY_SCORE(10006, "tech_vitality_score", "技术生命力"),
SSEIN_QIPING_TECH_VITALITY_INDUS_AVG(10007, "tech_vitality_indus_avg", "技术生命力"),
SSEIN_QIPING_RD_RATE_SCORE(10008, "rd_rate_score", "研发效率"),
SSEIN_QIPING_RD_RATE_INDUS_AVG(10009, "rd_rate_indus_avg", "研发效率"),
SSEIN_QIPING_RD_STABILITY_SCORE(10010, "rd_stability_score", "研发稳定性"),
SSEIN_QIPING_RD_STABILITY_INDUS_AVG(10011, "rd_stability_indus_avg", "研发稳定性"),
SSEIN_QIPING_INDUSTRY_RESEARCH_SCORE(10012, "industry_research_score", "产学研合作"),
SSEIN_QIPING_INDUSTRY_RESEARCH_INDUS_AVG(10013, "industry_research_indus_avg", "产学研合作"),
SSEIN_QIPING_GLOBAL_LAYOUT_SCORE(10014, "global_layout_score", "国际布局"),
SSEIN_QIPING_GLOBAL_LAYOUT_INDUS_AVG(10015, "global_layout_indus_avg", "国际布局"),
SSEIN_QIPING_CAPITAL_STRUCTURE_SCORE(10016, "capital_structure_score", "资本结构"),
SSEIN_QIPING_CAPITAL_STRUCTURE_INDUS_AVG(10017, "capital_structure_indus_avg", "资本结构"),
SSEIN_QIPING_PROFITABILITY_SCORE(10018, "profitability_score", "盈利能力score"),
SSEIN_QIPING_PROFITABILITY_INDUS_AVG(10019, "profitability_indus_avg", "盈利能力indus_avg"),
SSEIN_QIPING_GROWTH_ABILITY_SCORE(10020, "growth_ability_score", "成长能力"),
SSEIN_QIPING_GROWTH_ABILITY_INDUS_AVG(10021, "growth_ability_indus_avg", "成长能力"),
SSEIN_QIPING_FINANCIAL_RISK_SCORE(10022, "financial_risk_score", "财务风险"),
SSEIN_QIPING_FINANCIAL_RISK_INDUS_AVG(10023, "financial_risk_indus_avg", "财务风险"),
SSEIN_QIPING_PRODUCTION_ABILITY_SCORE(10024, "production_ability_score", "生产能力"),
SSEIN_QIPING_PRODUCTION_ABILITY_INDUS_AVG(10025, "production_ability_indus_avg", "生产能力"),
SSEIN_QIPING_SALES_ABILITY_SCORE(10026, "sales_ability_score", "销售能力"),
SSEIN_QIPING_SALES_ABILITY_INDUS_AVG(10027, "sales_ability_indus_avg", "销售能力"),
SSEIN_QIPING_EQUITY_CONCENTRATION_SCORE(10028, "equity_concentration_score", "股权集中程度"),
SSEIN_QIPING_EQUITY_CONCENTRATION_INDUS_AVG(10029, "equity_concentration_indus_avg", "股权集中程度"),
SSEIN_QIPING_FIRM_CONFIDENCE_SCORE(10030, "firm_confidence_score", "公司信心"),
SSEIN_QIPING_FIRM_CONFIDENCE_INDUS_AVG(10031, "firm_confidence_indus_avg", "公司信心"),
SSEIN_QIPING_INSTITUTION_OWNERSHIP_SCORE(10032, "institution_ownership_score", "机构持股"),
SSEIN_QIPING_INSTITUTION_OWNERSHIP_INDUS_AVG(10033, "institution_ownership_indus_avg", "机构持股"),
SSEIN_QIPING_CORPGOVERN_SCORE(10034, "corpgovern_score", "公司治理"),
SSEIN_QIPING_CORPGOVERN_INDUS_AVG(10035, "corpgovern_indus_avg", "公司治理"),
SSEIN_QIPING_DISCLOSURE_SCORE(10036, "disclosure_score", "信息披露"),
SSEIN_QIPING_DISCLOSURE_INDUS_AVG(10037, "disclosure_indus_avg", "信息披露"),
SSEIN_QIPING_RISKMGMT_SCORE(10038, "riskmgmt_score", "风险管理"),
SSEIN_QIPING_RISKMGMT_INDUS_AVG(10039, "riskmgmt_indus_avg", "风险管理"),
SSEIN_QIPING_BUSINETHICS_SCORE(10040, "businethics_score", "商业道德"),
SSEIN_QIPING_BUSINETHICS_INDUS_AVG(10041, "businethics_indus_avg", "商业道德"),
SSEIN_QIPING_GOVRNDISPUTE_SCORE(10042, "govrndispute_score", "治理争议事件"),
SSEIN_QIPING_GOVRNDISPUTE_INDUS_AVG(10043, "govrndispute_indus_avg", "治理争议事件"),
SSEIN_QIPING_ENVIRONMENT_SCORE(10044, "environment_score", "环境"),
SSEIN_QIPING_ENVIRONMENT_INDUS_AVG(10045, "environment_indus_avg", "环境"),
SSEIN_QIPING_SOCIETY_SCORE(10046, "society_score", "社会"),
SSEIN_QIPING_SOCIETY_INDUS_AVG(10047, "society_indus_avg", "社会"),
SSEIN_QIPING_ASSET_STRUCTURE_SCORE(10048, "asset_structure_score", "资产战略"),
SSEIN_QIPING_ASSET_STRUCTURE_INDUS_AVG(10049, "asset_structure_indus_avg", "资产战略"),
SSEIN_QIPING_DEBT_STRUCTURE_SCORE(10050, "debt_structure_score", "融资结构"),
SSEIN_QIPING_DEBT_STRUCTURE_INDUS_AVG(10051, "debt_structure_indus_avg", "融资结构"),
SSEIN_QIPING_OPERATING_RETURN_SCORE(10052, "operating_return_score", "业务回报"),
SSEIN_QIPING_OPERATING_RETURN_INDUS_AVG(10053, "operating_return_indus_avg", "业务回报"),
SSEIN_QIPING_CAPITAL_RETURN_SCORE(10054, "capital_return_score", "资本回报"),
SSEIN_QIPING_CAPITAL_RETURN_INDUS_AVG(10055, "capital_return_indus_avg", "资本回报"),
SSEIN_QIPING_SCALE_GROWTH_SCORE(10056, "scale_growth_score", "规模增长"),
SSEIN_QIPING_SCALE_GROWTH_INDUS_AVG(10057, "scale_growth_indus_avg", "规模增长"),
SSEIN_QIPING_INCOME_GROWTH_SCORE(10058, "income_growth_score", "收入增长"),
SSEIN_QIPING_INCOME_GROWTH_INDUS_AVG(10059, "income_growth_indus_avg", "收入增长"),
SSEIN_QIPING_CAPITAL_RISK_SCORE(10060, "capital_risk_score", "资本风险"),
SSEIN_QIPING_CAPITAL_RISK_INDUS_AVG(10061, "capital_risk_indus_avg", "资本风险"),
SSEIN_QIPING_OPERATING_RISK_SCORE(10062, "operating_risk_score", "经营风险"),
SSEIN_QIPING_OPERATING_RISK_INDUS_AVG(10063, "operating_risk_indus_avg", "经营风险"),
SSEIN_QIPING_PURCHASE_LINK_SCORE(10064, "purchase_link_score", "购货环节"),
SSEIN_QIPING_PURCHASE_LINK_INDUS_AVG(10065, "purchase_link_indus_avg", "购货环节"),
SSEIN_QIPING_PRODUCTION_LINK_SCORE(10066, "production_link_score", "生产环节"),
SSEIN_QIPING_PRODUCTION_LINK_INDUS_AVG(10067, "production_link_indus_avg", "生产环节"),
SSEIN_QIPING_INVENTORY_LINK_SCORE(10068, "inventory_link_score", "存货环节"),
SSEIN_QIPING_INVENTORY_LINK_INDUS_AVG(10069, "inventory_link_indus_avg", "存货环节"),
SSEIN_QIPING_SALES_LINK_SCORE(10070, "sales_link_score", "销货环节"),
SSEIN_QIPING_SALES_LINK_INDUS_AVG(10071, "sales_link_indus_avg", "销货环节"),
SSEIN_QIPING_TOP_SHAREHOLDER_OWNERSHIP_SCORE(10072, "top_shareholder_ownership_score", "最大股东控股"),
SSEIN_QIPING_TOP_SHAREHOLDER_OWNERSHIP_INDUS_AVG(10073, "top_shareholder_ownership_indus_avg", "最大股东控股"),
SSEIN_QIPING_MANAGER_LAYER_OWNERSHIP_SCORE(10074, "manager_layer_ownership_score", "管理层（董监高 ）持股"),
SSEIN_QIPING_MANAGER_LAYER_OWNERSHIP_INDUS_AVG(10075, "manager_layer_ownership_indus_avg", "管理层（董监高 ）持股"),
SSEIN_QIPING_OTHER_SHAREHOLDER_OWNERSHIP_SCORE(10076, "other_shareholder_ownership_score", "非控大股东持股"),
SSEIN_QIPING_OTHER_SHAREHOLDER_OWNERSHIP_INDUS_AVG(10077, "other_shareholder_ownership_indus_avg", "非控大股东持股"),
SSEIN_QIPING_REPURCHASE_AGREEMENT_SCORE(10078, "repurchase_agreement_score", "回购协议"),
SSEIN_QIPING_REPURCHASE_AGREEMENT_INDUS_AVG(10079, "repurchase_agreement_indus_avg", "回购协议"),
SSEIN_QIPING_DIVIDEND_SCORE(10080, "dividend_score", "公司分红"),
SSEIN_QIPING_DIVIDEND_INDUS_AVG(10081, "dividend_indus_avg", "公司分红"),
SSEIN_QIPING_EMPLOYEE_OWNERSHIP_SCORE(10082, "employee_ownership_score", "员工持股"),
SSEIN_QIPING_EMPLOYEE_OWNERSHIP_INDUS_AVG(10083, "employee_ownership_indus_avg", "员工持股"),
SSEIN_QIPING_FAMOUS_INSTITUTION_OWNERSHIP_SCORE(10084, "famous_institution_ownership_score", "知名机构投资"),
SSEIN_QIPING_FAMOUS_INSTITUTION_OWNERSHIP_INDUS_AVG(10085, "famous_institution_ownership_indus_avg", "知名机构投资"),
SSEIN_QIPING_PE_FINANCING_SCALE_SCORE(10086, "pe_financing_scale_score", "股权融资规模"),
SSEIN_QIPING_PE_FINANCING_SCALE_INDUS_AVG(10087, "pe_financing_scale_indus_avg", "股权融资规模"),
SSEIN_QIPING_ENMGMT_SCORE(10088, "enmgmt_score", "环境管理"),
SSEIN_QIPING_ENMGMT_INDUS_AVG(10089, "enmgmt_indus_avg", "环境管理"),
SSEIN_QIPING_RESOURCE_SCORE(10090, "resource_score", "能源和资源使用"),
SSEIN_QIPING_RESOURCE_INDUS_AVG(10091, "resource_indus_avg", "能源和资源使用"),
SSEIN_QIPING_WASTE_SCORE(10092, "waste_score", "废弃物"),
SSEIN_QIPING_WASTE_INDUS_AVG(10093, "waste_indus_avg", "废弃物"),
SSEIN_QIPING_ENOPPORTNTY_SCORE(10094, "enopportnty_score", "环境机遇"),
SSEIN_QIPING_ENOPPORTNTY_INDUS_AVG(10095, "enopportnty_indus_avg", "环境机遇"),
SSEIN_QIPING_ENDISPUTE_SCORE(10096, "endispute_score", "环境争议事件"),
SSEIN_QIPING_ENDISPUTE_INDUS_AVG(10097, "endispute_indus_avg", "环境争议事件"),
SSEIN_QIPING_PDCTLIABILITY_SCORE(10098, "pdctliability_score", "产品责任"),
SSEIN_QIPING_PDCTLIABILITY_INDUS_AVG(10099, "pdctliability_indus_avg", "产品责任"),
SSEIN_QIPING_LABORIGHT_SCORE(10100, "laboright_score", "劳工权益"),
SSEIN_QIPING_LABORIGHT_INDUS_AVG(10101, "laboright_indus_avg", "劳工权益"),
SSEIN_QIPING_HEALTHSAFETYS_SCORE(10102, "healthsafetys_score", "健康与安全"),
SSEIN_QIPING_HEALTHSAFETYS_INDUS_AVG(10103, "healthsafetys_indus_avg", "健康与安全"),
SSEIN_QIPING_EMDEVELOPMENT_SCORE(10104, "emdevelopment_score", "发展与培训"),
SSEIN_QIPING_EMDEVELOPMENT_INDUS_AVG(10105, "emdevelopment_indus_avg", "发展与培训"),
SSEIN_QIPING_SUPPLYMGMT_SCORE(10106, "supplymgmt_score", "供应链管理"),
SSEIN_QIPING_SUPPLYMGMT_INDUS_AVG(10107, "supplymgmt_indus_avg", "供应链管理"),
SSEIN_QIPING_SOCIALDISPUTE_SCORE(10108, "socialdispute_score", "社会争议事件"),
SSEIN_QIPING_SOCIALDISPUTE_INDUS_AVG(10109, "socialdispute_indus_avg", "社会争议事件"),
    '''
    data_list = raw2.strip().split(",\n")
    for data in data_list:
        enum_name = data.split("(")[0]
        data_value = data.split("(")[1][:-2]
        data_value_split = data_value.split(",")
        desc = data_value_split[2]
        # print( data_value_split[1].find("score"))
        if data_value_split[1].find("score") != -1:
            desc = desc + "分数"
        elif data_value_split[1].find("indus_avg") != -1:
            desc = desc + "行业均值"
        print(enum_name+"("+data_value_split[0] +","+ data_value_split[1] +","+ desc + "\"),")
    pass

def work3():
    tmp = Template('''SSEIN_QIPING_JSON_ARRAY_${id}(${idx}, "ssein_qiping_json_array_${id}", "ssein_qiping_json_array_${id}"),''')
    for i in range(0, 10):
        print(tmp.substitute(id=i, idx = 990000+i))
    pass

if __name__ == '__main__':
    work4()