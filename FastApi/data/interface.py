from FastApi.common.excel_handle import Excel

if __name__ == '__main__':
    data = {
        "swagger": "2.0",
        "info": {
            "description": "Api Documentation",
            "version": "1.0",
            "title": "Api Documentation",
            "termsOfService": "urn:tos",
            "contact": {

            },
            "license": {
                "name": "Apache 2.0",
                "url": "http://www.apache.org/licenses/LICENSE-2.0"
            }
        },
        "host": "172.30.1.24:8200",
        "basePath": "/",
        "tags": [{
            "name": "basic-error-controller",
            "description": "Basic Error Controller"
        },
            {
                "name": "互评-分数",
                "description": "Assessment Ctrl"
            },
            {
                "name": "任务业务层",
                "description": "User Task Ctrl"
            },
            {
                "name": "任务冲刺报告",
                "description": "Project Sprint Report Ctrl"
            },
            {
                "name": "其他-基础配置",
                "description": "Base Config Ctrl"
            },
            {
                "name": "其他-奖惩记录",
                "description": "Deal Ctrl"
            },
            {
                "name": "其他-评定标准与等级配置",
                "description": "Standard Config Ctrl"
            },
            {
                "name": "报表管理",
                "description": "Report Controller"
            },
            {
                "name": "文件上传",
                "description": "File Controller"
            },
            {
                "name": "文档管理",
                "description": "Doc Controller"
            },
            {
                "name": "用户-用户信息",
                "description": "User Controller"
            },
            {
                "name": "用户层",
                "description": "System Ctrl"
            },
            {
                "name": "用户评分报告",
                "description": "Project Sprint Member Report Ctrl"
            },
            {
                "name": "系统层-模板",
                "description": "System Temp Ctrl"
            },
            {
                "name": "系统层-模板优先级",
                "description": "System Temp Priorities Ctrl"
            },
            {
                "name": "系统层-模板状态",
                "description": "System Temp Status Ctrl"
            },
            {
                "name": "系统层-模板类型",
                "description": "System Temp Types Ctrl"
            },
            {
                "name": "系统层-模板角色",
                "description": "System Temp Roles Ctrl"
            },
            {
                "name": "级别基点值",
                "description": "Level Base Point Controller"
            },
            {
                "name": "考核-考核项",
                "description": "Assess Item Controller"
            },
            {
                "name": "考核指标",
                "description": "Assess Indicator Controller"
            },
            {
                "name": "考核通知",
                "description": "Assess Notice Ctrl"
            },
            {
                "name": "菜单管理",
                "description": "Menu Function Controller"
            },
            {
                "name": "角色管理",
                "description": "Role Controller"
            },
            {
                "name": "部门管理",
                "description": "Department Controller"
            },
            {
                "name": "项目业务层-任务",
                "description": "Project Task Ctrl"
            },
            {
                "name": "项目业务层-任务回复",
                "description": "Project Task Reply Ctrl"
            },
            {
                "name": "项目业务层-任务归档",
                "description": "Project Task Archive Ctrl"
            },
            {
                "name": "项目业务层-冲刺",
                "description": "Project Sprint Ctrl"
            },
            {
                "name": "项目业务层-计划",
                "description": "Project Plan Ctrl"
            },
            {
                "name": "项目业务层-项目",
                "description": "Project Ctrl"
            },
            {
                "name": "项目业务层-项目申请",
                "description": "Project Apply Ctrl"
            },
            {
                "name": "项目业务层-项目申请审批",
                "description": "Project Apply Approve Ctrl"
            },
            {
                "name": "项目招聘",
                "description": "Project Recruit Controller"
            },
            {
                "name": "项目经理考核-考核项记录",
                "description": "Assess Record Ctrl"
            },
            {
                "name": "项目经理考核报告",
                "description": "Manager Report Ctrl"
            },
            {
                "name": "项目设置层-任务/bug状态",
                "description": "Project Task Status Ctrl"
            },
            {
                "name": "项目设置层-任务优先级",
                "description": "Project Task Priority Ctrl"
            },
            {
                "name": "项目设置层-任务类型",
                "description": "Project Task Type Ctrl"
            },
            {
                "name": "项目设置层-项目人员",
                "description": "Project User Ctrl"
            },
            {
                "name": "项目设置层-项目角色",
                "description": "Project Role Ctrl"
            }],
        "paths": {
            "/api/task/assess": {
                "get": {
                    "tags": ["互评-分数"],
                    "summary": "查看互评结果/获取问题",
                    "operationId": "getAssessUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "query",
                        "description": "项目ID",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "score",
                            "in": "query",
                            "description": "分数",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/AssessmentVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["互评-分数"],
                    "summary": "保存互评",
                    "operationId": "saveAssessUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "query",
                        "description": "项目ID",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "score",
                            "in": "query",
                            "description": "分数",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/Assessment"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assess/item": {
                "delete": {
                    "tags": ["考核-考核项"],
                    "summary": "删除",
                    "operationId": "deleteAssessItemUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "itemIds",
                        "in": "query",
                        "description": "itemIds",
                        "required": False,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assess/item/assess/items": {
                "get": {
                    "tags": ["考核-考核项"],
                    "summary": "递归查询所有考核项及子集",
                    "operationId": "selectItemsUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«AssessItemRecursiveVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assess/item/items": {
                "get": {
                    "tags": ["考核-考核项"],
                    "summary": "递归查询某角色下的考核项及子集",
                    "operationId": "queryAssessItemByRoleUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«AssessItemRecursiveVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["考核-考核项"],
                    "summary": "新增",
                    "operationId": "saveAssessItemUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessType",
                        "in": "query",
                        "description": "考核类型,1:项目,2:项目管理人员",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "defaultScore",
                            "in": "query",
                            "description": "默认分",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "executorRole",
                            "in": "query",
                            "description": "执行人角色,1:开发人员,2:PM,3:职能人员,4:PMO,5:EPG,6:QA",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "itemName",
                            "in": "query",
                            "description": "考核项名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "parentId",
                            "in": "query",
                            "description": "父id",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«AssessItemVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assess/item/notice/role/items": {
                "get": {
                    "tags": ["考核通知"],
                    "summary": "查询某角色下的考核项",
                    "operationId": "getAssessItemByRoleUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessNoticeId",
                        "in": "query",
                        "description": "assessNoticeId",
                        "required": False,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«AssessNoticeItemVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assess/item/parent": {
                "get": {
                    "tags": ["考核-考核项"],
                    "summary": "查询所有父id为0的考核项",
                    "operationId": "queryAssessItemByParentIdUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«AssessItemRecursiveVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assess/item/{id}": {
                "get": {
                    "tags": ["考核-考核项"],
                    "summary": "根据主键查找",
                    "operationId": "queryAssessItemByPrimaryKeyUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "id",
                        "in": "path",
                        "description": "id",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«AssessItemVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "put": {
                    "tags": ["考核-考核项"],
                    "summary": "更新",
                    "operationId": "updateAssessItemUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessType",
                        "in": "query",
                        "description": "考核类型,1:项目,2:项目管理人员",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "defaultScore",
                            "in": "query",
                            "description": "默认分",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "executorRole",
                            "in": "query",
                            "description": "执行人角色,1:开发人员,2:PM,3:职能人员,4:PMO,5:EPG,6:QA",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "id",
                            "in": "path",
                            "description": "id",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "itemName",
                            "in": "query",
                            "description": "考核项名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "parentId",
                            "in": "query",
                            "description": "父id",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«AssessItemVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessIndicator/addConfig": {
                "post": {
                    "tags": ["考核指标"],
                    "summary": "新增指标项配置信息",
                    "operationId": "saveAssessIndicatorConfigUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessIndicatorId",
                        "in": "query",
                        "description": "考核指标id",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "assessIndicatorName",
                            "in": "query",
                            "description": "考核指标名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "baseScore",
                            "in": "query",
                            "description": "基点换算分",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "createTime",
                            "in": "query",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "id",
                            "in": "query",
                            "description": "主键id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "initialScore",
                            "in": "query",
                            "description": "初始分",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "qualifiedScore",
                            "in": "query",
                            "description": "合格分",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "updateTime",
                            "in": "query",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "userType",
                            "in": "query",
                            "description": "人员类别，1：开发人员；2：项目经理",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«AssessIndicatorConfig»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessIndicator/addDict": {
                "post": {
                    "tags": ["考核指标"],
                    "summary": "新增指标字典项",
                    "operationId": "saveAssessIndicatorDictUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessIndicatorId",
                        "in": "query",
                        "description": "考核指标Id",
                        "required": False,
                        "type": "integer",
                        "format": "int32",
                        "allowEmptyValue": False
                    },
                        {
                            "name": "assessIndicatorName",
                            "in": "query",
                            "description": "考核指标名称",
                            "required": False,
                            "type": "string",
                            "allowEmptyValue": False
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«AssessIndicatorDictVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessIndicator/configIsExist": {
                "get": {
                    "tags": ["考核指标"],
                    "summary": "判断考核项配置名称是否存在",
                    "operationId": "assessIndicatorConfigIsExistUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessIndicatorName",
                        "in": "query",
                        "description": "考核指标名称",
                        "required": False,
                        "type": "string",
                        "allowEmptyValue": False
                    },
                        {
                            "name": "userType",
                            "in": "query",
                            "description": "userType",
                            "required": False,
                            "type": "integer",
                            "format": "int32",
                            "allowEmptyValue": False
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessIndicator/deleteConfig": {
                "delete": {
                    "tags": ["考核指标"],
                    "summary": "删除指标项配置",
                    "operationId": "deleteAssessIndicatorConfigUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "id",
                        "in": "query",
                        "description": "主键id",
                        "required": False,
                        "type": "string",
                        "allowEmptyValue": False
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessIndicator/dictIsExist": {
                "get": {
                    "tags": ["考核指标"],
                    "summary": "判断考核项指标名称是否存在",
                    "operationId": "assessIndicatorDictNameIsExistUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessIndicatorName",
                        "in": "query",
                        "description": "考核指标名称",
                        "required": False,
                        "type": "string",
                        "allowEmptyValue": False
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessIndicator/getConfig": {
                "get": {
                    "tags": ["考核指标"],
                    "summary": "获取指标项配置信息",
                    "operationId": "queryAssessIndicatorConfigListUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«AssessIndicatorConfigVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessIndicator/getUserType": {
                "get": {
                    "tags": ["考核指标"],
                    "summary": "获取人员类别信息",
                    "operationId": "queryUserTypeUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«PersonalTypeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessIndicator/indicatorEnum": {
                "get": {
                    "tags": ["考核指标"],
                    "summary": "查询指标项枚举信息",
                    "operationId": "queryIndicatorEnumUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«Map«string,int»»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessIndicator/list": {
                "get": {
                    "tags": ["考核指标"],
                    "summary": "查询指标项字典信息",
                    "operationId": "queryAssessIndicatorListUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«AssessIndicatorDictVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessIndicator/updateDict": {
                "patch": {
                    "tags": ["考核指标"],
                    "summary": "更新指标字典项",
                    "operationId": "updateAssessIndicatorDictUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessIndicatorName",
                        "in": "query",
                        "description": "考核指标名称",
                        "required": False,
                        "type": "string",
                        "allowEmptyValue": False
                    },
                        {
                            "name": "id",
                            "in": "query",
                            "description": "主键Id",
                            "required": False,
                            "type": "string",
                            "allowEmptyValue": False
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«AssessIndicatorDict»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessIndicator/updateScore": {
                "patch": {
                    "tags": ["考核指标"],
                    "summary": "更新分值",
                    "operationId": "updateScoreUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessIndicatorId",
                        "in": "query",
                        "description": "考核指标id",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "assessIndicatorName",
                            "in": "query",
                            "description": "考核指标名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "baseScore",
                            "in": "query",
                            "description": "基点换算分",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "createTime",
                            "in": "query",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "id",
                            "in": "query",
                            "description": "主键id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "initialScore",
                            "in": "query",
                            "description": "初始分",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "qualifiedScore",
                            "in": "query",
                            "description": "合格分",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "updateTime",
                            "in": "query",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "userType",
                            "in": "query",
                            "description": "人员类别，1：开发人员；2：项目经理",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«AssessIndicatorConfig»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessNotice": {
                "get": {
                    "tags": ["考核通知"],
                    "summary": "查询通知列表",
                    "operationId": "getNoticeListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«AssessNoticeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["考核通知"],
                    "summary": "保存通知",
                    "operationId": "saveNoticeUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessItemList",
                        "in": "query",
                        "description": "考核项集合",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "assessStatus",
                            "in": "query",
                            "description": "考核状态（0：未完成，1：已完成，2：已取消）",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "assessTimeEnd",
                            "in": "query",
                            "description": "考核截至时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "assessTimeStart",
                            "in": "query",
                            "description": "考核开始时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "description",
                            "in": "query",
                            "description": "描述",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "noticeName",
                            "in": "query",
                            "description": "通知名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "query",
                            "description": "项目id",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«AssessNoticeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessNotice/assessChange": {
                "get": {
                    "tags": ["考核通知"],
                    "summary": "redis消息通知-查看",
                    "operationId": "assessChangeUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["考核通知"],
                    "summary": "redis消息通知-修改",
                    "operationId": "setAssessChangeUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "data",
                        "in": "query",
                        "description": "data",
                        "required": False,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessNotice/execute/{assessNoticeId}": {
                "get": {
                    "tags": ["考核通知"],
                    "summary": "考核执行列表查询",
                    "operationId": "getExecuteListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessNoticeId",
                        "in": "path",
                        "description": "assessNoticeId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«Pair«string,List«NoticeItemVO»»»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessNotice/manager": {
                "get": {
                    "tags": ["考核通知"],
                    "summary": "项目经理查询自己通知列表",
                    "operationId": "getManagerNoticeListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«AssessNoticeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessNotice/{id}": {
                "delete": {
                    "tags": ["考核通知"],
                    "summary": "删除通知",
                    "operationId": "deleteNoticeUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "id",
                        "in": "path",
                        "description": "id",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["考核通知"],
                    "summary": "修改通知",
                    "operationId": "updateNoticeUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessItemList",
                        "in": "query",
                        "description": "考核项集合",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "assessStatus",
                            "in": "query",
                            "description": "考核状态（0：未完成，1：已完成，2：已取消）",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "assessTimeEnd",
                            "in": "query",
                            "description": "考核截至时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "assessTimeStart",
                            "in": "query",
                            "description": "考核开始时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "description",
                            "in": "query",
                            "description": "描述",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "id",
                            "in": "path",
                            "description": "id",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "noticeName",
                            "in": "query",
                            "description": "通知名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "query",
                            "description": "项目id",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«AssessNoticeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessRecord": {
                "post": {
                    "tags": ["项目经理考核-考核项记录"],
                    "summary": "保存考核项",
                    "operationId": "saveRecordUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessRecordForm",
                        "in": "query",
                        "description": "assessRecordForm",
                        "required": False,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/assessRecord/{assessNoticeId}": {
                "get": {
                    "tags": ["项目经理考核-考核项记录"],
                    "summary": "查看考核记录",
                    "operationId": "getRecordListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "assessNoticeId",
                        "in": "path",
                        "description": "assessNoticeId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "currentPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«Pair«string,List«AssessRecordVO»»»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/basecfg": {
                "get": {
                    "tags": ["其他-基础配置"],
                    "summary": "获取基础配置列表",
                    "operationId": "getBaseConfigUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/BaseConfigVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["其他-基础配置"],
                    "summary": "添加基础配置",
                    "operationId": "createBaseConfigUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "addedScore",
                        "in": "query",
                        "description": "附加奖励分数",
                        "required": False,
                        "type": "number"
                    },
                        {
                            "name": "assessProportion",
                            "in": "query",
                            "description": "评价占比",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "flowerScore",
                            "in": "query",
                            "description": "小红花奖励点数",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "fullDayPoints",
                            "in": "query",
                            "description": "饱和点数",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "punishScore",
                            "in": "query",
                            "description": "惩罚分数",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "shareScore",
                            "in": "query",
                            "description": "分享奖励分数",
                            "required": False,
                            "type": "number"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/BaseConfigVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/basecfg/insertDates/{year}": {
                "post": {
                    "tags": ["其他-基础配置"],
                    "summary": "存储当年节假日、调休日",
                    "operationId": "insertDatesUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "year",
                        "in": "path",
                        "description": "year",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/basecfg/{basecfgId}": {
                "delete": {
                    "tags": ["其他-基础配置"],
                    "summary": "删除基础配置",
                    "operationId": "deleteBaseConfigUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "basecfgId",
                        "in": "path",
                        "description": "basecfgId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["其他-基础配置"],
                    "summary": "修改基础配置",
                    "operationId": "updateBaseConfigUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "addedScore",
                        "in": "query",
                        "description": "附加奖励分数",
                        "required": False,
                        "type": "number"
                    },
                        {
                            "name": "assessProportion",
                            "in": "query",
                            "description": "评价占比",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "basecfgId",
                            "in": "path",
                            "description": "basecfgId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "flowerScore",
                            "in": "query",
                            "description": "小红花奖励点数",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "fullDayPoints",
                            "in": "query",
                            "description": "饱和点数",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "punishScore",
                            "in": "query",
                            "description": "惩罚分数",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "shareScore",
                            "in": "query",
                            "description": "分享奖励分数",
                            "required": False,
                            "type": "number"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/BaseConfigVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/levelBasePoint/list": {
                "get": {
                    "tags": ["级别基点值"],
                    "summary": "级别基点信息列表",
                    "operationId": "queryLevelPointListUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«LevelBasePoint»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/levelBasePoint/refreshLevel": {
                "get": {
                    "tags": ["级别基点值"],
                    "summary": "刷新级别信息",
                    "operationId": "refreshLevelListUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«LevelBasePoint»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/levelBasePoint/updatePoint": {
                "patch": {
                    "tags": ["级别基点值"],
                    "summary": "更新分值",
                    "operationId": "updatePointUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "basePoint",
                        "in": "query",
                        "description": "基点",
                        "required": True,
                        "type": "number"
                    },
                        {
                            "name": "createTime",
                            "in": "query",
                            "description": "创建时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "evaluateQualifiedScore",
                            "in": "query",
                            "description": "互评合格分",
                            "required": True,
                            "type": "number"
                        },
                        {
                            "name": "id",
                            "in": "query",
                            "description": "主键id",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "levelId",
                            "in": "query",
                            "description": "级别id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "levelName",
                            "in": "query",
                            "description": "级别名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "updateTime",
                            "in": "query",
                            "description": "更新时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«LevelBasePoint»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/manageReport/month": {
                "get": {
                    "tags": ["项目经理考核报告"],
                    "summary": "createManagerReport",
                    "operationId": "createManagerReportUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/manageReport/pm": {
                "get": {
                    "tags": ["项目经理考核报告"],
                    "summary": "项目经理查看考核报告",
                    "operationId": "getManagerReportForPMUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "endDate",
                            "in": "query",
                            "description": "结束日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "startDate",
                            "in": "query",
                            "description": "开始日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ManagerReportVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/manageReport/pmo": {
                "get": {
                    "tags": ["项目经理考核报告"],
                    "summary": "PMO查看考核报告",
                    "operationId": "getManagerReportForPMOUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "endDate",
                            "in": "query",
                            "description": "结束日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "startDate",
                            "in": "query",
                            "description": "开始日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ManagerReportVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/manageReport/projectUserScoreReport": {
                "get": {
                    "tags": ["项目经理考核报告"],
                    "summary": "查询指定项目的用户得分报告",
                    "operationId": "queryProjectUserScoreReportUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "query",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«UserScoreReportVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/manageReport/{managerReportId}/detail": {
                "get": {
                    "tags": ["项目经理考核报告"],
                    "summary": "查看考核报告明细",
                    "operationId": "getReportDetailUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "managerReportId",
                        "in": "path",
                        "description": "managerReportId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«AssessRecordVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/mine/tasks": {
                "get": {
                    "tags": ["任务业务层"],
                    "summary": "获取我的任务",
                    "operationId": "mineTasksUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«UserTaskVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/mine/tasks/status": {
                "get": {
                    "tags": ["任务业务层"],
                    "summary": "获取任务状态列表",
                    "operationId": "getTaskStatusUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/mine/tasks/summary": {
                "get": {
                    "tags": ["任务业务层"],
                    "summary": "获取本周任务",
                    "operationId": "getTaskCountAndSumUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskCountAndSumVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/project/recruit": {
                "get": {
                    "tags": ["项目招聘"],
                    "summary": "获取所有开关打开的项目招聘列表",
                    "operationId": "getOpenProjectRecruitUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectRecruitVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["项目招聘"],
                    "summary": "添加项目招聘",
                    "operationId": "createProjectRecruitUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "endTime",
                        "in": "query",
                        "description": "结束招聘时间",
                        "required": False,
                        "type": "string",
                        "format": "date-time"
                    },
                        {
                            "name": "openFlag",
                            "in": "query",
                            "description": "招聘开关（0：关，1：开）",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "postDescription",
                            "in": "query",
                            "description": "职位描述",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "postJobShare",
                            "in": "query",
                            "description": "要求占比",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "postName",
                            "in": "query",
                            "description": "职位名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "postSum",
                            "in": "query",
                            "description": "招聘人数",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "postType",
                            "in": "query",
                            "description": "职位类型（1：Java后端，2：Web前端，3：手机前端，4：小程序，5：UI，6：测试）",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "proRoleId",
                            "in": "query",
                            "description": "角色id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "query",
                            "description": "项目id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "startTime",
                            "in": "query",
                            "description": "开始招聘时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectRecruitVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/project/recruit/": {
                "get": {
                    "tags": ["项目招聘"],
                    "summary": "获取所有项目下的项目招聘信息",
                    "operationId": "getRecruitPositionUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "description": "currentPage",
                        "required": False,
                        "type": "integer",
                        "default": 1,
                        "format": "int32"
                    },
                        {
                            "name": "perPage",
                            "in": "query",
                            "description": "perPage",
                            "required": False,
                            "type": "integer",
                            "default": 10,
                            "format": "int32"
                        },
                        {
                            "name": "postType",
                            "in": "query",
                            "description": "postType",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectAndRecruitVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/project/recruit/{recruitId}": {
                "get": {
                    "tags": ["项目招聘"],
                    "summary": "获取项目招聘",
                    "operationId": "getProjectRecruitUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "recruitId",
                        "in": "path",
                        "description": "recruitId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectRecruitVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "delete": {
                    "tags": ["项目招聘"],
                    "summary": "删除项目招聘",
                    "operationId": "deleteProjectRecruitUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "recruitId",
                        "in": "path",
                        "description": "recruitId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "boolean"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["项目招聘"],
                    "summary": "修改项目招聘",
                    "operationId": "updateProjectRecruitUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "endTime",
                        "in": "query",
                        "description": "结束招聘时间",
                        "required": False,
                        "type": "string",
                        "format": "date-time"
                    },
                        {
                            "name": "openFlag",
                            "in": "query",
                            "description": "招聘开关（0：关，1：开）",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "postDescription",
                            "in": "query",
                            "description": "职位描述",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "postJobShare",
                            "in": "query",
                            "description": "要求占比",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "postName",
                            "in": "query",
                            "description": "职位名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "postSum",
                            "in": "query",
                            "description": "招聘人数",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "postType",
                            "in": "query",
                            "description": "职位类型（1：Java后端，2：Web前端，3：手机前端，4：小程序，5：UI，6：测试）",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "proRoleId",
                            "in": "query",
                            "description": "角色id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "query",
                            "description": "项目id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "recruitId",
                            "in": "path",
                            "description": "recruitId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "startTime",
                            "in": "query",
                            "description": "开始招聘时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectRecruitVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/project/{projectId}/deals": {
                "get": {
                    "tags": ["其他-奖惩记录"],
                    "summary": "获取项目奖惩记录",
                    "operationId": "getProjectDealsUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "description": "currentPage",
                        "required": False,
                        "type": "integer",
                        "default": 1,
                        "format": "int32"
                    },
                        {
                            "name": "perPage",
                            "in": "query",
                            "description": "perPage",
                            "required": False,
                            "type": "integer",
                            "default": 10,
                            "format": "int32"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«DealTaskVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/project/{projectId}/mine/report": {
                "get": {
                    "tags": ["用户评分报告"],
                    "summary": "个人报告",
                    "operationId": "getProjectUserReportUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectMemberReportVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/project/{projectId}/project/recruit/": {
                "get": {
                    "tags": ["项目招聘"],
                    "summary": "获取项目下的项目及项目招聘信息",
                    "operationId": "getProjectRecruitInfoUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectAndRecruitVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/project/{projectId}/recruit/": {
                "get": {
                    "tags": ["项目招聘"],
                    "summary": "获取项目下的项目招聘职位",
                    "operationId": "getProjectRecruitPositionUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectRecruitVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/project/{projectId}/sprints/{sprintId}/member/{memberReportId}/report": {
                "put": {
                    "tags": ["用户评分报告"],
                    "summary": "更新用户评分报告",
                    "operationId": "updateProjectSprintMemberReportUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "attScore",
                        "in": "query",
                        "description": "att分数",
                        "required": False,
                        "type": "number",
                        "format": "double"
                    },
                        {
                            "name": "finishCount",
                            "in": "query",
                            "description": "任务结束总数",
                            "required": False,
                            "type": "integer",
                            "format": "int64"
                        },
                        {
                            "name": "finishPoints",
                            "in": "query",
                            "description": "结束点数",
                            "required": False,
                            "type": "number",
                            "format": "double"
                        },
                        {
                            "name": "memberReportId",
                            "in": "path",
                            "description": "memberReportId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "month",
                            "in": "query",
                            "description": "月",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "pointTotal",
                            "in": "query",
                            "description": "总点数",
                            "required": False,
                            "type": "number",
                            "format": "double"
                        },
                        {
                            "name": "projectId",
                            "in": "query",
                            "description": "项目id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "remark",
                            "in": "query",
                            "description": "标记",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "score",
                            "in": "query",
                            "description": "分数",
                            "required": False,
                            "type": "number",
                            "format": "double"
                        },
                        {
                            "name": "sprintId",
                            "in": "query",
                            "description": "冲刺id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "taskCount",
                            "in": "query",
                            "description": "任务总数",
                            "required": False,
                            "type": "integer",
                            "format": "int64"
                        },
                        {
                            "name": "userId",
                            "in": "query",
                            "description": "用户id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "week",
                            "in": "query",
                            "description": "周",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "year",
                            "in": "query",
                            "description": "年",
                            "required": False,
                            "type": "integer",
                            "format": "int64"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectSprintMemberReportVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/project/{projectId}/sprints/{sprintId}/member/{userId}/report": {
                "get": {
                    "tags": ["用户评分报告"],
                    "summary": "个人报告",
                    "operationId": "getMemberReportUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "sprintId",
                            "in": "path",
                            "description": "sprintId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "userId",
                            "in": "path",
                            "description": "userId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectSprintMemberReportVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/project/{projectId}/sprints/{sprintId}/reports": {
                "get": {
                    "tags": ["任务冲刺报告"],
                    "summary": "冲刺报告详情",
                    "operationId": "getSprintDetailUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "sprintId",
                            "in": "path",
                            "description": "sprintId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectSprintReportVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/all": {
                "get": {
                    "tags": ["项目业务层-项目"],
                    "summary": "获取所有未终止项目列表",
                    "operationId": "getManagerProjectListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/apply": {
                "get": {
                    "tags": ["项目业务层-项目申请"],
                    "summary": "查看申请列表",
                    "operationId": "findAppliesUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectApplyVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["项目业务层-项目申请"],
                    "summary": "项目申请",
                    "operationId": "projectApplyUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "applyStatus",
                        "in": "query",
                        "description": "申请状态",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "applyType",
                            "in": "query",
                            "description": "申请类型",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "applyUserDescription",
                            "in": "query",
                            "description": "申请人描述",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "applyUserId",
                            "in": "query",
                            "description": "申请用户id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "query",
                            "description": "项目id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "recruitId",
                            "in": "query",
                            "description": "招聘id",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectApplyVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/approve/current": {
                "get": {
                    "tags": ["项目业务层-项目申请审批"],
                    "summary": "当前项目组审核展示待审核列表",
                    "operationId": "nowProjectShowUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectApplyApproveVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/assess": {
                "get": {
                    "tags": ["项目业务层-项目"],
                    "summary": "获取所有待考核的项目列表",
                    "operationId": "getAssessProjectUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/users": {
                "get": {
                    "tags": ["项目设置层-项目人员"],
                    "summary": "获取项目经理",
                    "operationId": "getManagerUserUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectManagerVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{applyId}/approve": {
                "get": {
                    "tags": ["项目业务层-项目申请审批"],
                    "summary": "获取当前申请审批列表",
                    "operationId": "getApproveByApplyIdUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "applyId",
                        "in": "path",
                        "description": "申请ID",
                        "required": False,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectApplyApproveVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{approveId}/approve": {
                "patch": {
                    "tags": ["项目业务层-项目申请审批"],
                    "summary": "审核",
                    "operationId": "applyUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "approveDescription",
                        "in": "query",
                        "description": "审核意见",
                        "required": False,
                        "type": "string",
                        "allowEmptyValue": False
                    },
                        {
                            "name": "approveId",
                            "in": "path",
                            "description": "审核ID",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "approveStatus",
                            "in": "query",
                            "description": "审核状态（0:审核中、1：已审批、2：已驳回）",
                            "required": False,
                            "type": "string",
                            "allowEmptyValue": False
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectApplyApproveVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/active/sprints/tasks": {
                "get": {
                    "tags": ["项目业务层-任务"],
                    "summary": "获取正在执行的冲刺任务",
                    "operationId": "getActiveSprintTaskUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/approve/goal": {
                "get": {
                    "tags": ["项目业务层-项目申请审批"],
                    "summary": "目标项目组审核展示待审核列表",
                    "operationId": "goalProjectShowUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "项目ID",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectApplyApproveVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/bug/status": {
                "get": {
                    "tags": ["项目设置层-任务/bug状态"],
                    "summary": "查找bug状态",
                    "operationId": "getBugStatusUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "bugFlag",
                        "in": "query",
                        "description": "bugFlag",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["项目设置层-任务/bug状态"],
                    "summary": "添加bug状态",
                    "operationId": "createBugStatusUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "bugFlag",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "serial",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "statusColor",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "statusName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "statusType",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/bug/status/{taskStatusId}": {
                "delete": {
                    "tags": ["项目设置层-任务/bug状态"],
                    "summary": "删除bug状态",
                    "operationId": "deleteBugStatusUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "taskStatusId",
                            "in": "path",
                            "description": "taskStatusId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["项目设置层-任务/bug状态"],
                    "summary": "修改bug状态",
                    "operationId": "updateBugStatusUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "bugFlag",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "serial",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "statusColor",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "statusName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "statusType",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "taskStatusId",
                            "in": "path",
                            "description": "taskStatusId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/deal": {
                "get": {
                    "tags": ["其他-奖惩记录"],
                    "summary": "获取奖惩记录列表",
                    "operationId": "getDealUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«DealVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/deals": {
                "get": {
                    "tags": ["其他-奖惩记录"],
                    "summary": "获取人员奖惩记录",
                    "operationId": "getDealsUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/Map«string,object»"
                                }
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/finished/sprints": {
                "get": {
                    "tags": ["项目业务层-冲刺"],
                    "summary": "获取已完成冲刺列表",
                    "operationId": "getFinishedSprintUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectSprintVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/index/data": {
                "get": {
                    "tags": ["项目业务层-任务"],
                    "summary": "获取项目首页数据",
                    "operationId": "getProjectIndexDataUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ProjectTaskIndexVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/page/users": {
                "get": {
                    "tags": ["项目设置层-项目人员"],
                    "summary": "分页获取项目用户列表",
                    "operationId": "getPageProjectUserUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "description": "currentPage",
                        "required": False,
                        "type": "integer",
                        "default": 1,
                        "format": "int32"
                    },
                        {
                            "name": "perPage",
                            "in": "query",
                            "description": "perPage",
                            "required": False,
                            "type": "integer",
                            "default": 10,
                            "format": "int32"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«User»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/plans": {
                "get": {
                    "tags": ["项目业务层-计划"],
                    "summary": "获取项目计划列表",
                    "operationId": "getProjectPlanListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "limitFlag",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "status",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectPlanVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["项目业务层-计划"],
                    "summary": "创建项目计划",
                    "operationId": "createProjectPlanDetailUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "desc",
                        "in": "query",
                        "description": "计划描述",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "endTime",
                            "in": "query",
                            "description": "截止日期",
                            "required": True,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "name",
                            "in": "query",
                            "description": "计划名称",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "startTime",
                            "in": "query",
                            "description": "开始日期",
                            "required": True,
                            "type": "string",
                            "format": "date-time"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectPlanVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/plans/{planId}": {
                "get": {
                    "tags": ["项目业务层-计划"],
                    "summary": "获取项目计划详情",
                    "operationId": "getProjectPlanDetailUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "limitFlag",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "planId",
                            "in": "path",
                            "description": "planId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "status",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectPlanVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "put": {
                    "tags": ["项目业务层-计划"],
                    "summary": "修改项目计划",
                    "operationId": "updateProjectPlanDetailUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "desc",
                        "in": "query",
                        "description": "计划描述",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "endTime",
                            "in": "query",
                            "description": "截止日期",
                            "required": True,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "name",
                            "in": "query",
                            "description": "计划名称",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "planId",
                            "in": "path",
                            "description": "planId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "startTime",
                            "in": "query",
                            "description": "开始日期",
                            "required": True,
                            "type": "string",
                            "format": "date-time"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectPlanVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "delete": {
                    "tags": ["项目业务层-计划"],
                    "summary": "删除项目计划详情",
                    "operationId": "deleteProjectPlanDetailUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "planId",
                        "in": "path",
                        "description": "planId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/plans/{planId}/archive": {
                "post": {
                    "tags": ["项目业务层-计划"],
                    "summary": "归档项目计划",
                    "operationId": "archiveProjectPlanUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "list",
                        "in": "query",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "planId",
                            "in": "path",
                            "description": "planId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/plans/{planId}/members": {
                "get": {
                    "tags": ["项目业务层-计划"],
                    "summary": "获取项目计划列表",
                    "operationId": "getProjectPlanMembersUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "planId",
                        "in": "path",
                        "description": "planId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectPlanMemberVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/plans/{planId}/status": {
                "put": {
                    "tags": ["项目业务层-计划"],
                    "summary": "修改项目计划状态",
                    "operationId": "updateProjectPlanStatusUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "planId",
                        "in": "path",
                        "description": "planId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "status",
                            "in": "query",
                            "description": "status",
                            "required": True,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/priorities": {
                "get": {
                    "tags": ["项目设置层-任务优先级"],
                    "summary": "获取优先级列表",
                    "operationId": "getPrioritiesUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskPriorityVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["项目设置层-任务优先级"],
                    "summary": "添加优先级",
                    "operationId": "createPriorityUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "defaultMark",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "priorityColor",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "priorityName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskPriorityVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/priorities/{taskPriorityId}": {
                "delete": {
                    "tags": ["项目设置层-任务优先级"],
                    "summary": "删除优先级",
                    "operationId": "deletePriorityUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "taskPriorityId",
                            "in": "path",
                            "description": "taskPriorityId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskPriorityVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["项目设置层-任务优先级"],
                    "summary": "更新优先级",
                    "operationId": "updatePriorityUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "defaultMark",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "priorityColor",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "priorityName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "taskPriorityId",
                            "in": "path",
                            "description": "taskPriorityId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskPriorityVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/roles": {
                "get": {
                    "tags": ["项目设置层-项目角色"],
                    "summary": "查找角色",
                    "operationId": "getRolesUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectRoleVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["项目设置层-项目角色"],
                    "summary": "增加角色",
                    "operationId": "createRoleUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "cancelSprint",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "createSprint",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "createTask",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "manage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "roleLogoType",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "roleName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "updateTask",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "updatedSprint",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectRoleVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/roles/{proRoleId}": {
                "delete": {
                    "tags": ["项目设置层-项目角色"],
                    "summary": "删除角色",
                    "operationId": "deleteRoleUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "proRoleId",
                        "in": "path",
                        "description": "proRoleId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectRoleVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["项目设置层-项目角色"],
                    "summary": "修改角色",
                    "operationId": "updateRoleUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "cancelSprint",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "createSprint",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "createTask",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "manage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "proRoleId",
                            "in": "path",
                            "description": "proRoleId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "roleLogoType",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "roleName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "updateTask",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "updatedSprint",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectRoleVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/sprints": {
                "get": {
                    "tags": ["项目业务层-冲刺"],
                    "summary": "获取冲刺列表",
                    "operationId": "getSprintUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectSprintVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["项目业务层-冲刺"],
                    "summary": "添加冲刺",
                    "operationId": "createSprintUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectSprintVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/sprints/{sprintId}": {
                "delete": {
                    "tags": ["项目业务层-冲刺"],
                    "summary": "删除冲刺",
                    "operationId": "deleteSprintUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "sprintId",
                            "in": "path",
                            "description": "sprintId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/sprints/{sprintId}/active": {
                "patch": {
                    "tags": ["项目业务层-冲刺"],
                    "summary": "修改冲刺为进行中",
                    "operationId": "updateSprintUpdateUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "sprintId",
                            "in": "path",
                            "description": "sprintId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/sprints/{sprintId}/finished": {
                "patch": {
                    "tags": ["项目业务层-冲刺"],
                    "summary": "修改冲刺为已结束",
                    "operationId": "updateSprintFinishedUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "sprintId",
                            "in": "path",
                            "description": "sprintId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/sprints/{sprintId}/tasks": {
                "post": {
                    "tags": ["项目业务层-任务"],
                    "summary": "创建冲刺任务",
                    "operationId": "createSprintUsingPOST_1",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "archive",
                        "in": "query",
                        "description": "是否完结：0，1",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "broTaskId",
                            "in": "query",
                            "description": "关联任务id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "bugStatusId",
                            "in": "query",
                            "description": "bug类型id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "countedPoints",
                            "in": "query",
                            "description": "有效点数",
                            "required": False,
                            "type": "number",
                            "format": "double"
                        },
                        {
                            "name": "creatorId",
                            "in": "query",
                            "description": "任务创建者id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "deadLine",
                            "in": "query",
                            "description": "截止日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "description",
                            "in": "query",
                            "description": "任务描述",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "executorId",
                            "in": "query",
                            "description": "任务执行人id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "finishedAt",
                            "in": "query",
                            "description": "任务结束时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "parTaskId",
                            "in": "query",
                            "description": "父任务id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "planId",
                            "in": "query",
                            "description": "计划id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "points",
                            "in": "query",
                            "description": "任务点数",
                            "required": False,
                            "type": "number",
                            "format": "double"
                        },
                        {
                            "name": "priceFlag",
                            "in": "query",
                            "description": "是否悬赏任务：0，1",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "priorityId",
                            "in": "query",
                            "description": "任务优先级id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "sprintId",
                            "in": "path",
                            "description": "sprintId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "startedAt",
                            "in": "query",
                            "description": "任务开始时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "statusId",
                            "in": "query",
                            "description": "任务状态id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "taskGetDateLine",
                            "in": "query",
                            "description": "任务领取截至日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "title",
                            "in": "query",
                            "description": "任务标题",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "typeId",
                            "in": "query",
                            "description": "任务类型id",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectTaskVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/status": {
                "get": {
                    "tags": ["项目设置层-任务/bug状态"],
                    "summary": "查找任务状态",
                    "operationId": "getStatusUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "bugFlag",
                        "in": "query",
                        "description": "bugFlag",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["项目设置层-任务/bug状态"],
                    "summary": "添加任务状态",
                    "operationId": "createStatusUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "bugFlag",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "serial",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "statusColor",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "statusName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "statusType",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/status/{taskStatusId}": {
                "delete": {
                    "tags": ["项目设置层-任务/bug状态"],
                    "summary": "删除任务状态",
                    "operationId": "deleteStatusUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "taskStatusId",
                            "in": "path",
                            "description": "taskStatusId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["项目设置层-任务/bug状态"],
                    "summary": "修改任务状态",
                    "operationId": "updateStatusUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "bugFlag",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "serial",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "statusColor",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "statusName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "statusType",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "taskStatusId",
                            "in": "path",
                            "description": "taskStatusId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/tasks": {
                "get": {
                    "tags": ["项目业务层-任务"],
                    "summary": "获取任务",
                    "operationId": "getTaskListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "archive",
                        "in": "query",
                        "description": "完结状态，0:未完结，1:已完结，为1时，分配任务和执行标记失效",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "assign",
                            "in": "query",
                            "description": "是否分配",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "bugStatusId",
                            "in": "query",
                            "description": "bug状态id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "dateEnd",
                            "in": "query",
                            "description": "结束日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "dateStart",
                            "in": "query",
                            "description": "开始日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "executorId",
                            "in": "query",
                            "description": "执行人员",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "limit",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "offset",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "page",
                            "in": "query",
                            "description": "每页数量",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "perPage",
                            "in": "query",
                            "description": "每页数量",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "planId",
                            "in": "query",
                            "description": "计划id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "query",
                            "description": "项目id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "statusId",
                            "in": "query",
                            "description": "任务状态id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "typeId",
                            "in": "query",
                            "description": "类型",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["项目业务层-任务"],
                    "summary": "创建任务",
                    "operationId": "createSprintUsingPOST_2",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "archive",
                        "in": "query",
                        "description": "是否完结：0，1",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "broTaskId",
                            "in": "query",
                            "description": "关联任务id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "bugStatusId",
                            "in": "query",
                            "description": "bug类型id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "countedPoints",
                            "in": "query",
                            "description": "有效点数",
                            "required": False,
                            "type": "number",
                            "format": "double"
                        },
                        {
                            "name": "creatorId",
                            "in": "query",
                            "description": "任务创建者id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "deadLine",
                            "in": "query",
                            "description": "截止日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "description",
                            "in": "query",
                            "description": "任务描述",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "executorId",
                            "in": "query",
                            "description": "任务执行人id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "finishedAt",
                            "in": "query",
                            "description": "任务结束时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "parTaskId",
                            "in": "query",
                            "description": "父任务id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "planId",
                            "in": "query",
                            "description": "计划id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "points",
                            "in": "query",
                            "description": "任务点数",
                            "required": False,
                            "type": "number",
                            "format": "double"
                        },
                        {
                            "name": "priceFlag",
                            "in": "query",
                            "description": "是否悬赏任务：0，1",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "priorityId",
                            "in": "query",
                            "description": "任务优先级id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "startedAt",
                            "in": "query",
                            "description": "任务开始时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "statusId",
                            "in": "query",
                            "description": "任务状态id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "taskGetDateLine",
                            "in": "query",
                            "description": "任务领取截至日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "title",
                            "in": "query",
                            "description": "任务标题",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "typeId",
                            "in": "query",
                            "description": "任务类型id",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/tasks/{taskId}": {
                "get": {
                    "tags": ["项目业务层-任务"],
                    "summary": "获取任务详情",
                    "operationId": "getTaskDetailUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectTaskVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "put": {
                    "tags": ["项目业务层-任务"],
                    "summary": "修改任务",
                    "operationId": "updateTaskUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "archive",
                        "in": "query",
                        "description": "是否完结：0，1",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "broTaskId",
                            "in": "query",
                            "description": "关联任务id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "bugStatusId",
                            "in": "query",
                            "description": "bug类型id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "countedPoints",
                            "in": "query",
                            "description": "有效点数",
                            "required": False,
                            "type": "number",
                            "format": "double"
                        },
                        {
                            "name": "creatorId",
                            "in": "query",
                            "description": "任务创建者id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "deadLine",
                            "in": "query",
                            "description": "截止日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "description",
                            "in": "query",
                            "description": "任务描述",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "executorId",
                            "in": "query",
                            "description": "任务执行人id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "finishedAt",
                            "in": "query",
                            "description": "任务结束时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "parTaskId",
                            "in": "query",
                            "description": "父任务id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "planId",
                            "in": "query",
                            "description": "计划id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "points",
                            "in": "query",
                            "description": "任务点数",
                            "required": False,
                            "type": "number",
                            "format": "double"
                        },
                        {
                            "name": "priceFlag",
                            "in": "query",
                            "description": "是否悬赏任务：0，1",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "priorityId",
                            "in": "query",
                            "description": "任务优先级id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "startedAt",
                            "in": "query",
                            "description": "任务开始时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "statusId",
                            "in": "query",
                            "description": "任务状态id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "taskGetDateLine",
                            "in": "query",
                            "description": "任务领取截至日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "title",
                            "in": "query",
                            "description": "任务标题",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "typeId",
                            "in": "query",
                            "description": "任务类型id",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectTaskVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "delete": {
                    "tags": ["项目业务层-任务"],
                    "summary": "删除任务",
                    "operationId": "deleteTaskUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/tasks/{taskId}/archive": {
                "put": {
                    "tags": ["项目业务层-任务"],
                    "summary": "任务完结",
                    "operationId": "archiveTaskUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/tasks/{taskId}/copy": {
                "put": {
                    "tags": ["项目业务层-任务"],
                    "summary": "复制任务",
                    "operationId": "copyArchiveUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectTaskVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/tasks/{taskId}/priceTask": {
                "put": {
                    "tags": ["项目业务层-任务"],
                    "summary": "悬赏任务领取",
                    "operationId": "priceTaskUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/tasks/{taskId}/replies": {
                "get": {
                    "tags": ["项目业务层-任务回复"],
                    "summary": "获取任务回复列表",
                    "operationId": "getTaskRepliesListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskReplyVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["项目业务层-任务回复"],
                    "summary": "创建任务评论",
                    "operationId": "createTaskCommentUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "content",
                        "in": "query",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "oratorId",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ProjectTaskReplyVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/tasks/{taskId}/reply/{replyId}": {
                "delete": {
                    "tags": ["项目业务层-任务回复"],
                    "summary": "删除评论",
                    "operationId": "deleteTaskCommentUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "replyId",
                            "in": "path",
                            "description": "replyId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["项目业务层-任务回复"],
                    "summary": "修改任务评论",
                    "operationId": "updateTaskCommentUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "content",
                        "in": "query",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "oratorId",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "replyId",
                            "in": "path",
                            "description": "replyId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ProjectTaskReplyVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/tasks/{taskId}/sprint/{sprintId}": {
                "patch": {
                    "tags": ["项目业务层-任务"],
                    "summary": "修改任务冲刺",
                    "operationId": "updateTaskSprintUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "sprintId",
                            "in": "path",
                            "description": "sprintId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectTaskVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/tasks/{taskId}/task": {
                "put": {
                    "tags": ["项目业务层-任务"],
                    "summary": "普通任务领取",
                    "operationId": "commonTaskUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/tasks/{taskId}/user/{userId}/deal": {
                "post": {
                    "tags": ["其他-奖惩记录"],
                    "summary": "任务添加小红花",
                    "operationId": "createRedFlowerUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "dealType",
                        "in": "query",
                        "description": "类型",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "remark",
                            "in": "query",
                            "description": "备注",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "score",
                            "in": "query",
                            "description": "分数",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "userId",
                            "in": "path",
                            "description": "userId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«DealVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/tasks/{taskId}/{statusId}": {
                "put": {
                    "tags": ["项目业务层-任务"],
                    "summary": "任务状态变更",
                    "operationId": "updateTaskStatusUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "statusId",
                            "in": "path",
                            "description": "statusId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "taskId",
                            "in": "path",
                            "description": "taskId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«string»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/types": {
                "get": {
                    "tags": ["项目设置层-任务类型"],
                    "summary": "查找类别",
                    "operationId": "getTypeUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskTypeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["项目设置层-任务类型"],
                    "summary": "增加类别",
                    "operationId": "createTypeUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "typeLogo",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "typeName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskTypeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/types/{taskTypeId}": {
                "delete": {
                    "tags": ["项目设置层-任务类型"],
                    "summary": "删除类别",
                    "operationId": "deleteTypeUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "taskTypeId",
                            "in": "path",
                            "description": "taskTypeId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskTypeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["项目设置层-任务类型"],
                    "summary": "修改类别",
                    "operationId": "updateTypeUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "taskTypeId",
                            "in": "path",
                            "description": "taskTypeId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "typeLogo",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "typeName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectTaskTypeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/user/{userId}/deal": {
                "get": {
                    "tags": ["其他-奖惩记录"],
                    "summary": "获取项目下某个参与人员的奖惩记录列表",
                    "operationId": "getDealByUserIdUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "userId",
                            "in": "path",
                            "description": "userId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«DealVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["其他-奖惩记录"],
                    "summary": "添加奖惩记录",
                    "operationId": "createDealUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "dealType",
                        "in": "query",
                        "description": "类型",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "remark",
                            "in": "query",
                            "description": "备注",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "score",
                            "in": "query",
                            "description": "分数",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "userId",
                            "in": "path",
                            "description": "userId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«DealVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/userInfo": {
                "get": {
                    "tags": ["项目设置层-项目人员"],
                    "summary": "获取项目成员信息",
                    "operationId": "getProjectUserInfoUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«Map«string,object»»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/users": {
                "get": {
                    "tags": ["项目设置层-项目人员"],
                    "summary": "获取项目用户列表",
                    "operationId": "getProjectUserUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«User»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/users/{userId}": {
                "delete": {
                    "tags": ["项目设置层-项目人员"],
                    "summary": "删除项目用户角色",
                    "operationId": "deleteProjectUserUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "userId",
                            "in": "path",
                            "description": "userId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«User»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/users/{userId}/role/{roleId}": {
                "post": {
                    "tags": ["项目设置层-项目人员"],
                    "summary": "添加项目用户",
                    "operationId": "createProjectUserWithRoleUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "percent",
                        "in": "query",
                        "description": "percent",
                        "required": True,
                        "type": "number"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "roleId",
                            "in": "path",
                            "description": "roleId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "userId",
                            "in": "path",
                            "description": "userId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«User»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["项目设置层-项目人员"],
                    "summary": "修改项目用户角色",
                    "operationId": "updateProjectUserToRoleUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "percent",
                        "in": "query",
                        "description": "percent",
                        "required": True,
                        "type": "number"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "roleId",
                            "in": "path",
                            "description": "roleId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "userId",
                            "in": "path",
                            "description": "userId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«User»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/projects/{projectId}/web/hook": {
                "get": {
                    "tags": ["项目业务层-任务回复"],
                    "summary": "获取项目WebHook",
                    "operationId": "getProjectWebHookUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ProjectWebHookVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "put": {
                    "tags": ["项目业务层-任务回复"],
                    "summary": "修改项目WebHook",
                    "operationId": "updateProjectWebHookUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "projectId",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "triggerCancel",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "triggerCreate",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "triggerFinished",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "triggerUpdate",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "webAccess",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "webSecret",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "webUrl",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ProjectWebHookVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/report/month": {
                "get": {
                    "tags": ["报表管理"],
                    "summary": "month----",
                    "operationId": "monthUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/report/user/{userId}/project": {
                "get": {
                    "tags": ["报表管理"],
                    "summary": "获取个人项目",
                    "operationId": "getUserProjectUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "userId",
                        "in": "path",
                        "description": "userId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/Map«string,object»"
                                }
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/report/{userId}/{projectId}": {
                "get": {
                    "tags": ["报表管理"],
                    "summary": "个人工作报告",
                    "operationId": "userProjectReportUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "userId",
                            "in": "path",
                            "description": "userId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«PersonalProjectWorkVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/search": {
                "get": {
                    "tags": ["文档管理"],
                    "summary": "全局查询文档",
                    "operationId": "searchUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "allOnly",
                        "in": "query",
                        "required": False,
                        "type": "boolean"
                    },
                        {
                            "name": "createrOnly",
                            "in": "query",
                            "required": False,
                            "type": "boolean"
                        },
                        {
                            "name": "fileEnd",
                            "in": "query",
                            "description": "文件后缀",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "pageNum",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "projectOnly",
                            "in": "query",
                            "required": False,
                            "type": "boolean"
                        },
                        {
                            "name": "searchkey",
                            "in": "query",
                            "description": "关键字",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "size",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«DocVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/standardcfg": {
                "get": {
                    "tags": ["其他-评定标准与等级配置"],
                    "summary": "获取评定标准与等级配置列表",
                    "operationId": "getStandardConfigUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«StandardConfigVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["其他-评定标准与等级配置"],
                    "summary": "添加评定标准与等级配置",
                    "operationId": "createStandardConfigUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "endPoint",
                        "in": "query",
                        "description": "止分",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "standardLevel",
                            "in": "query",
                            "description": "等级",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "startPoint",
                            "in": "query",
                            "description": "起分",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«StandardConfigVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/standardcfg/{levelId}": {
                "delete": {
                    "tags": ["其他-评定标准与等级配置"],
                    "summary": "删除评定标准与等级配置",
                    "operationId": "deleteStandardConfigUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "levelId",
                        "in": "path",
                        "description": "levelId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["其他-评定标准与等级配置"],
                    "summary": "修改评定标准与等级配置",
                    "operationId": "updateStandardConfigUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "endPoint",
                        "in": "query",
                        "description": "止分",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "levelId",
                            "in": "path",
                            "description": "levelId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "standardLevel",
                            "in": "query",
                            "description": "等级",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "startPoint",
                            "in": "query",
                            "description": "起分",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«StandardConfigVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/department": {
                "post": {
                    "tags": ["部门管理"],
                    "summary": "添加部门",
                    "operationId": "addDepartmentUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "description",
                        "in": "query",
                        "description": "部门描述",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "level",
                            "in": "query",
                            "description": "部门层级",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "name",
                            "in": "query",
                            "description": "部门名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "parentId",
                            "in": "query",
                            "description": "上级部门ID",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "parentName",
                            "in": "query",
                            "description": "上级部门名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "remark",
                            "in": "query",
                            "description": "备注",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "sortNumber",
                            "in": "query",
                            "description": "排序",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "status",
                            "in": "query",
                            "description": "启用状态",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«Department»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/department/getByPage": {
                "get": {
                    "tags": ["部门管理"],
                    "summary": "分页查询部门列表",
                    "operationId": "getByPageUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "pageNum",
                        "in": "query",
                        "description": "页码",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "pageSize",
                            "in": "query",
                            "description": "条数",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "description": "查询关键字",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«Department»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/department/{primaryKey}": {
                "get": {
                    "tags": ["部门管理"],
                    "summary": "根据主键查询",
                    "operationId": "getDepartmentByKeyUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "primaryKey",
                        "in": "path",
                        "description": "primaryKey",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«Department»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "delete": {
                    "tags": ["部门管理"],
                    "summary": "删除部门",
                    "operationId": "deleteDepartmentUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "primaryKey",
                        "in": "path",
                        "description": "primaryKey",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "boolean"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["部门管理"],
                    "summary": "修改部门",
                    "operationId": "updateDepartmentUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "description",
                        "in": "query",
                        "description": "部门描述",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "level",
                            "in": "query",
                            "description": "部门层级",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "name",
                            "in": "query",
                            "description": "部门名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "parentId",
                            "in": "query",
                            "description": "上级部门ID",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "parentName",
                            "in": "query",
                            "description": "上级部门名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "primaryKey",
                            "in": "path",
                            "description": "primaryKey",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "remark",
                            "in": "query",
                            "description": "备注",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "sortNumber",
                            "in": "query",
                            "description": "排序",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "status",
                            "in": "query",
                            "description": "启用状态",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«Department»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/departments": {
                "get": {
                    "tags": ["部门管理"],
                    "summary": "查询部门列表",
                    "operationId": "getDepartmentListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "pageNum",
                        "in": "query",
                        "description": "页码",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "pageSize",
                            "in": "query",
                            "description": "条数",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "description": "查询关键字",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«Department»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/departments/all": {
                "get": {
                    "tags": ["用户层"],
                    "summary": "获取全部部门",
                    "operationId": "getAllDepartmentUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«DepartmentVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/departments/{departId}/users": {
                "get": {
                    "tags": ["用户层"],
                    "summary": "获取部门全部用户",
                    "operationId": "getDepartmentAllUserUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "departId",
                        "in": "path",
                        "description": "departId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«User»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/menu": {
                "post": {
                    "tags": ["菜单管理"],
                    "summary": "新增菜单",
                    "operationId": "addMenuFunctionUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "component",
                        "in": "query",
                        "description": "菜单项对应请求路径",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "desciption",
                            "in": "query",
                            "description": "描述",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "menuLevel",
                            "in": "query",
                            "description": "菜单项层级",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "name",
                            "in": "query",
                            "description": "名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "parentId",
                            "in": "query",
                            "description": "父级ID",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "remark",
                            "in": "query",
                            "description": "备注",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "requestMode",
                            "in": "query",
                            "description": "请求方式",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "shortCutIcon",
                            "in": "query",
                            "description": "图标",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "sortNumber",
                            "in": "query",
                            "description": "排序号",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "description": "类型",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "visible",
                            "in": "query",
                            "description": "是否显示",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«MenuFunction»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/menu/getByPage": {
                "get": {
                    "tags": ["菜单管理"],
                    "summary": "分页查询菜单",
                    "operationId": "getByPageUsingGET_1",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "pageNum",
                        "in": "query",
                        "description": "页码",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "pageSize",
                            "in": "query",
                            "description": "条数",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "description": "查询关键字",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«MenuFunction»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/menu/{primaryKey}": {
                "get": {
                    "tags": ["菜单管理"],
                    "summary": "主键查找菜单",
                    "operationId": "getMenuFunctionByKeyUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "primaryKey",
                        "in": "path",
                        "description": "primaryKey",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«MenuFunction»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "delete": {
                    "tags": ["菜单管理"],
                    "summary": "删除菜单",
                    "operationId": "deleteByPrimaryKeyUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "primaryKey",
                        "in": "path",
                        "description": "primaryKey",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "boolean"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["菜单管理"],
                    "summary": "更新菜单",
                    "operationId": "updateMenuFunctionUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "component",
                        "in": "query",
                        "description": "菜单项对应请求路径",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "desciption",
                            "in": "query",
                            "description": "描述",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "menuLevel",
                            "in": "query",
                            "description": "菜单项层级",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "name",
                            "in": "query",
                            "description": "名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "parentId",
                            "in": "query",
                            "description": "父级ID",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "primaryKey",
                            "in": "path",
                            "description": "primaryKey",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "remark",
                            "in": "query",
                            "description": "备注",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "requestMode",
                            "in": "query",
                            "description": "请求方式",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "shortCutIcon",
                            "in": "query",
                            "description": "图标",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "sortNumber",
                            "in": "query",
                            "description": "排序号",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "description": "类型",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "visible",
                            "in": "query",
                            "description": "是否显示",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«MenuFunction»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/menuRole/{primaryKey}": {
                "get": {
                    "tags": ["角色管理"],
                    "summary": "查询角色下菜单列表",
                    "operationId": "getMenuRoleUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "primaryKey",
                        "in": "path",
                        "description": "primaryKey",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SimpleMenuResp»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/menuTree": {
                "get": {
                    "tags": ["菜单管理"],
                    "summary": "按树结构查询菜单",
                    "operationId": "getMenuFunctionForTreeUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "searchId",
                        "in": "query",
                        "description": "父节点id/部门id",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "description": "关键字",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "systemId",
                            "in": "query",
                            "description": "系统id",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«MenuFunction»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/menus": {
                "get": {
                    "tags": ["菜单管理"],
                    "summary": "查询菜单",
                    "operationId": "getMenuFunctionListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "pageNum",
                        "in": "query",
                        "description": "页码",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "pageSize",
                            "in": "query",
                            "description": "条数",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "description": "查询关键字",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«MenuFunction»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/role": {
                "post": {
                    "tags": ["角色管理"],
                    "summary": "新增角色",
                    "operationId": "addRoleUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "name",
                        "in": "query",
                        "description": "角色名称",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "note",
                            "in": "query",
                            "description": "批注",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "remark",
                            "in": "query",
                            "description": "备注",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "description": "类型",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«Role»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/role/getByPage": {
                "get": {
                    "tags": ["角色管理"],
                    "summary": "分页查询角色",
                    "operationId": "getByPageUsingGET_2",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "pageNum",
                        "in": "query",
                        "description": "页码",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "pageSize",
                            "in": "query",
                            "description": "条数",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "description": "查询关键字",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«Role»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/role/{primaryKey}": {
                "get": {
                    "tags": ["角色管理"],
                    "summary": "主键查找角色",
                    "operationId": "getRoleByKeyUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "primaryKey",
                        "in": "path",
                        "description": "primaryKey",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«Role»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "delete": {
                    "tags": ["角色管理"],
                    "summary": "删除角色",
                    "operationId": "deleteRoleUsingDELETE_1",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "primaryKey",
                        "in": "path",
                        "description": "primaryKey",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "boolean"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["角色管理"],
                    "summary": "更新角色",
                    "operationId": "updateByPrimaryKeySelectiveUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "name",
                        "in": "query",
                        "description": "角色名称",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "note",
                            "in": "query",
                            "description": "批注",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "primaryKey",
                            "in": "path",
                            "description": "primaryKey",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "remark",
                            "in": "query",
                            "description": "备注",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "description": "类型",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«Role»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/roles": {
                "get": {
                    "tags": ["角色管理"],
                    "summary": "查询角色",
                    "operationId": "getRoleListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "pageNum",
                        "in": "query",
                        "description": "页码",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "pageSize",
                            "in": "query",
                            "description": "条数",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "description": "查询关键字",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«Role»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/temp/{tempId}/priorities": {
                "get": {
                    "tags": ["系统层-模板优先级"],
                    "summary": "查询系统模板优先级列表",
                    "operationId": "getSystemTempPrioritiesUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "tempId",
                        "in": "path",
                        "description": "tempId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempPriorityVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["系统层-模板优先级"],
                    "summary": "创建系统模板优先级",
                    "operationId": "createSystemTempPrioritiesUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "defaultMark",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "priorityColor",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "priorityName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "tempId",
                            "in": "path",
                            "description": "tempId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempPriorityVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/temp/{tempId}/priorities/{priorityId}": {
                "delete": {
                    "tags": ["系统层-模板优先级"],
                    "summary": "删除系统模板优先级",
                    "operationId": "deleteSystemTempPrioritiesUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "priorityId",
                        "in": "path",
                        "description": "priorityId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "tempId",
                            "in": "path",
                            "description": "tempId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempPriorityVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["系统层-模板优先级"],
                    "summary": "修改系统模板优先级",
                    "operationId": "updateSystemTempPrioritiesUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "defaultMark",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "priorityColor",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "priorityId",
                            "in": "path",
                            "description": "priorityId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "priorityName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "tempId",
                            "in": "path",
                            "description": "tempId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempPriorityVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/temp/{tempId}/roles": {
                "get": {
                    "tags": ["系统层-模板角色"],
                    "summary": "查询系统模板角色列表",
                    "operationId": "getSystemTempRolesUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "tempId",
                        "in": "path",
                        "description": "tempId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempRoleVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["系统层-模板角色"],
                    "summary": "创建系统模板角色",
                    "operationId": "createSystemTempRolesUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "cancelSprint",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "createSprint",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "createTask",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "manage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "roleLogoType",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "roleName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "tempId",
                            "in": "path",
                            "description": "tempId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "updateTask",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "updatedSprint",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempRoleVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/temp/{tempId}/roles/{roleId}": {
                "delete": {
                    "tags": ["系统层-模板角色"],
                    "summary": "删除系统模板角色",
                    "operationId": "deleteSystemTempRolesUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "roleId",
                        "in": "path",
                        "description": "roleId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "tempId",
                            "in": "path",
                            "description": "tempId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempRoleVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["系统层-模板角色"],
                    "summary": "修改系统模板角色",
                    "operationId": "updateSystemTempRolesUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "cancelSprint",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "createSprint",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "createTask",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "manage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "roleId",
                            "in": "path",
                            "description": "roleId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "roleLogoType",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "roleName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "tempId",
                            "in": "path",
                            "description": "tempId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "updateTask",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "updatedSprint",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempRoleVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/temp/{tempId}/status": {
                "get": {
                    "tags": ["系统层-模板状态"],
                    "summary": "查询系统模板状态列表",
                    "operationId": "getSystemTempTypesUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "tempId",
                        "in": "path",
                        "description": "tempId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["系统层-模板状态"],
                    "summary": "创建系统模板状态",
                    "operationId": "createSystemTempStatusUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "serial",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "statusColor",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "statusName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "tempId",
                            "in": "path",
                            "description": "tempId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/temp/{tempId}/status/{statusId}": {
                "delete": {
                    "tags": ["系统层-模板状态"],
                    "summary": "删除系统模板状态",
                    "operationId": "deleteSystemTempStatusUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "statusId",
                        "in": "path",
                        "description": "statusId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "tempId",
                            "in": "path",
                            "description": "tempId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["系统层-模板状态"],
                    "summary": "修改系统模板状态",
                    "operationId": "updateSystemTempStatusUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "serial",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "statusColor",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "statusId",
                            "in": "path",
                            "description": "statusId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "statusName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "tempId",
                            "in": "path",
                            "description": "tempId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempStatusVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/temp/{tempId}/types": {
                "get": {
                    "tags": ["系统层-模板类型"],
                    "summary": "查询系统模板类型列表",
                    "operationId": "getSystemTempTypesUsingGET_1",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "tempId",
                        "in": "path",
                        "description": "tempId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempTypeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["系统层-模板类型"],
                    "summary": "创建系统模板类型",
                    "operationId": "createSystemTempTypesUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "tempId",
                        "in": "path",
                        "description": "tempId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "typeLogo",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "typeName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempTypeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/temp/{tempId}/types/{typeId}": {
                "put": {
                    "tags": ["系统层-模板类型"],
                    "summary": "修改系统模板类型",
                    "operationId": "updateSystemTempTypesUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "tempId",
                        "in": "path",
                        "description": "tempId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "typeId",
                            "in": "path",
                            "description": "typeId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "typeLogo",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "typeName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempTypeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "delete": {
                    "tags": ["系统层-模板类型"],
                    "summary": "删除系统模板类型",
                    "operationId": "deleteSystemTempTypesUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "tempId",
                        "in": "path",
                        "description": "tempId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "typeId",
                            "in": "path",
                            "description": "typeId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempTypeVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/temps": {
                "get": {
                    "tags": ["系统层-模板"],
                    "summary": "获取系统模板列表",
                    "operationId": "getSystemTempsUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«SystemTempVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["系统层-模板"],
                    "summary": "创建系统模板",
                    "operationId": "createSystemTempUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "tempImg",
                        "in": "query",
                        "description": "模板图片",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "tempName",
                            "in": "query",
                            "description": "模板名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "tempRemark",
                            "in": "query",
                            "description": "模板描述",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/SystemTempVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/system/temps/{tempId}": {
                "get": {
                    "tags": ["系统层-模板"],
                    "summary": "获取系统模板详情",
                    "operationId": "getSystemTempDetailUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "tempId",
                        "in": "path",
                        "description": "tempId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/SystemTempVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "delete": {
                    "tags": ["系统层-模板"],
                    "summary": "创建系统模板",
                    "operationId": "deleteSystemTempUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "tempId",
                        "in": "path",
                        "description": "tempId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["系统层-模板"],
                    "summary": "创建系统模板",
                    "operationId": "updateSystemTempUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "tempId",
                        "in": "path",
                        "description": "tempId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "tempImg",
                            "in": "query",
                            "description": "模板图片",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "tempName",
                            "in": "query",
                            "description": "模板名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "tempRemark",
                            "in": "query",
                            "description": "模板描述",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/SystemTempVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/export": {
                "get": {
                    "tags": ["用户-用户信息"],
                    "summary": "导出",
                    "operationId": "exportReportUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK"
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/info": {
                "get": {
                    "tags": ["用户层"],
                    "summary": "获取登录用户用户信息",
                    "operationId": "getUserInfoUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "key",
                        "in": "query",
                        "description": "key",
                        "required": False,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«User»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/page": {
                "get": {
                    "tags": ["用户-用户信息"],
                    "summary": "分页查询",
                    "operationId": "queryUserForPageUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "description": "currentPage",
                        "required": False,
                        "type": "integer",
                        "default": 1,
                        "format": "int32"
                    },
                        {
                            "name": "pageSize",
                            "in": "query",
                            "description": "pageSize",
                            "required": False,
                            "type": "integer",
                            "default": 10,
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "description": "searchKey",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«WorkerVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/projects": {
                "get": {
                    "tags": ["项目业务层-项目"],
                    "summary": "获取用户项目列表",
                    "operationId": "getUserProjectListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["项目业务层-项目"],
                    "summary": "用户创建项目",
                    "operationId": "createUserProjectUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "description",
                        "in": "query",
                        "description": "项目描述",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "endTime",
                            "in": "query",
                            "description": "结束时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "logo",
                            "in": "query",
                            "description": "项目logo",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectName",
                            "in": "query",
                            "description": "项目名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "startTime",
                            "in": "query",
                            "description": "开始时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "tempId",
                            "in": "query",
                            "description": "模板id",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ProjectVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/projects/{projectId}": {
                "get": {
                    "tags": ["项目业务层-项目"],
                    "summary": "获取项目详情",
                    "operationId": "getUserProjectDetailUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "put": {
                    "tags": ["项目业务层-项目"],
                    "summary": "用户修改项目",
                    "operationId": "updateUserProjectUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "description",
                        "in": "query",
                        "description": "项目描述",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "endTime",
                            "in": "query",
                            "description": "结束时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "logo",
                            "in": "query",
                            "description": "项目logo",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "projectName",
                            "in": "query",
                            "description": "项目名称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "startTime",
                            "in": "query",
                            "description": "开始时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ProjectVO"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/projects/{projectId}/archive": {
                "patch": {
                    "tags": ["项目业务层-项目"],
                    "summary": "项目完结",
                    "operationId": "archiveUserProjectUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/projects/{projectId}/disable": {
                "patch": {
                    "tags": ["项目业务层-项目"],
                    "summary": "用户终止项目",
                    "operationId": "disabledUserProjectUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/projects/{projectId}/enable": {
                "patch": {
                    "tags": ["项目业务层-项目"],
                    "summary": "用户恢复项目",
                    "operationId": "enabledUserProjectUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/reports": {
                "get": {
                    "tags": ["报表管理"],
                    "summary": "个人报表",
                    "operationId": "userReportUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "reportName",
                        "in": "query",
                        "description": "reportName",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ReportVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/reports/date": {
                "get": {
                    "tags": ["报表管理"],
                    "summary": "获取个人报告综合下拉菜单",
                    "operationId": "getUserReportDateUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«string»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/update/password": {
                "put": {
                    "tags": ["用户-用户信息"],
                    "summary": "修改个人密码",
                    "operationId": "userInfoPwdPutUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "newPassword",
                        "in": "query",
                        "description": "newPassword",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "password",
                            "in": "query",
                            "description": "password",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/user": {
                "get": {
                    "tags": ["用户-用户信息"],
                    "summary": "根据主键查找",
                    "operationId": "queryUserByPrimaryKeyUsingGET",
                    "produces": ["*/*"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«UserVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["用户-用户信息"],
                    "summary": "新增",
                    "operationId": "saveUserUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "birthDate",
                        "in": "query",
                        "description": "出生日期",
                        "required": False,
                        "type": "string",
                        "format": "date-time"
                    },
                        {
                            "name": "degree",
                            "in": "query",
                            "description": "学位",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "department",
                            "in": "query",
                            "description": "部门",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "educationBackground",
                            "in": "query",
                            "description": "学历",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "employedDate",
                            "in": "query",
                            "description": "入职日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "employeeCategory",
                            "in": "query",
                            "description": "员工类别",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "gender",
                            "in": "query",
                            "description": "性别,0:女,1:男",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "graduationDate",
                            "in": "query",
                            "description": "毕业日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "graduationSchool",
                            "in": "query",
                            "description": "毕业学校",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "idNumber",
                            "in": "query",
                            "description": "身份证号码",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "nation",
                            "in": "query",
                            "description": "民族",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "nativePlace",
                            "in": "query",
                            "description": "籍贯",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "phoneNumber",
                            "in": "query",
                            "description": "手机号码",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "politicsStatus",
                            "in": "query",
                            "description": "政治面貌",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "position",
                            "in": "query",
                            "description": "职务",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "profession",
                            "in": "query",
                            "description": "专业",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "role",
                            "in": "query",
                            "description": "角色,1:开发人员,2:PM,3:职能人员,4:PMO,5:EPG,6:QA",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "skillsTalents",
                            "in": "query",
                            "description": "技能特长",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "title",
                            "in": "query",
                            "description": "职称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "userName",
                            "in": "query",
                            "description": "姓名",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "workExperience",
                            "in": "query",
                            "description": "工作经验",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "workingYear",
                            "in": "query",
                            "description": "工作年限",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«UserVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/user/info": {
                "put": {
                    "tags": ["用户-用户信息"],
                    "summary": "更新",
                    "operationId": "updateUserUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "birthDate",
                        "in": "query",
                        "description": "出生日期",
                        "required": False,
                        "type": "string",
                        "format": "date-time"
                    },
                        {
                            "name": "degree",
                            "in": "query",
                            "description": "学位",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "department",
                            "in": "query",
                            "description": "部门",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "educationBackground",
                            "in": "query",
                            "description": "学历",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "employedDate",
                            "in": "query",
                            "description": "入职日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "employeeCategory",
                            "in": "query",
                            "description": "员工类别",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "gender",
                            "in": "query",
                            "description": "性别,0:女,1:男",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "graduationDate",
                            "in": "query",
                            "description": "毕业日期",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "graduationSchool",
                            "in": "query",
                            "description": "毕业学校",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "idNumber",
                            "in": "query",
                            "description": "身份证号码",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "nation",
                            "in": "query",
                            "description": "民族",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "nativePlace",
                            "in": "query",
                            "description": "籍贯",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "phoneNumber",
                            "in": "query",
                            "description": "手机号码",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "politicsStatus",
                            "in": "query",
                            "description": "政治面貌",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "position",
                            "in": "query",
                            "description": "职务",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "profession",
                            "in": "query",
                            "description": "专业",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "role",
                            "in": "query",
                            "description": "角色,1:开发人员,2:PM,3:职能人员,4:PMO,5:EPG,6:QA",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "skillsTalents",
                            "in": "query",
                            "description": "技能特长",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "title",
                            "in": "query",
                            "description": "职称",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "userName",
                            "in": "query",
                            "description": "姓名",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "workExperience",
                            "in": "query",
                            "description": "工作经验",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "workingYear",
                            "in": "query",
                            "description": "工作年限",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«UserVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/user/role/{id}": {
                "put": {
                    "tags": ["用户-用户信息"],
                    "summary": "修改角色",
                    "operationId": "updateUserUsingPUT_1",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "id",
                        "in": "path",
                        "description": "id",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "role",
                            "in": "query",
                            "description": "role",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«UserVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/user/{id}": {
                "delete": {
                    "tags": ["用户-用户信息"],
                    "summary": "删除",
                    "operationId": "deleteUserUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "id",
                        "in": "path",
                        "description": "id",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/users": {
                "get": {
                    "tags": ["项目设置层-项目人员"],
                    "summary": "获取分页获取用户",
                    "operationId": "getPlateUserUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "departmentIds",
                        "in": "query",
                        "required": False,
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "collectionFormat": "multi"
                    },
                        {
                            "name": "page",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "roleIds",
                            "in": "query",
                            "required": False,
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "collectionFormat": "multi"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "status",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "systemId",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "userIds",
                            "in": "query",
                            "required": False,
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "collectionFormat": "multi"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«User»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/users/{userId}/archived/tasks": {
                "get": {
                    "tags": ["项目业务层-任务归档"],
                    "summary": "获取用户任务归档",
                    "operationId": "getUserArchiveTaskUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "date",
                        "in": "query",
                        "description": "搜索日期",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "page",
                            "in": "query",
                            "description": "页数",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "perPage",
                            "in": "query",
                            "description": "每页个数",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "projectId",
                            "in": "query",
                            "description": "归档项目id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "description": "搜索关键字",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "userId",
                            "in": "path",
                            "description": "userId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectArchiveTaskVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/users/{userId}/projects": {
                "get": {
                    "tags": ["项目业务层-项目"],
                    "summary": "获取用户项目列表",
                    "operationId": "getUserAllProjectListUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "currentPage",
                        "in": "query",
                        "required": False,
                        "type": "integer",
                        "format": "int32"
                    },
                        {
                            "name": "perPage",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "searchKey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "type",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "userId",
                            "in": "path",
                            "description": "userId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«ProjectVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/{id}": {
                "put": {
                    "tags": ["任务冲刺报告"],
                    "summary": "更新",
                    "operationId": "updateProjectSprintReportUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "createdAt",
                        "in": "query",
                        "description": "创建时间",
                        "required": False,
                        "type": "string",
                        "format": "date-time"
                    },
                        {
                            "name": "endTime",
                            "in": "query",
                            "description": "结束时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "finishPoints",
                            "in": "query",
                            "description": "结束点数",
                            "required": False,
                            "type": "number"
                        },
                        {
                            "name": "finishTask",
                            "in": "query",
                            "description": "结束任务数量",
                            "required": False,
                            "type": "integer",
                            "format": "int64"
                        },
                        {
                            "name": "id",
                            "in": "path",
                            "description": "id",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "memberCount",
                            "in": "query",
                            "description": "用户数量",
                            "required": False,
                            "type": "integer",
                            "format": "int64"
                        },
                        {
                            "name": "pointTotal",
                            "in": "query",
                            "description": "总点数",
                            "required": False,
                            "type": "number",
                            "format": "double"
                        },
                        {
                            "name": "projectId",
                            "in": "query",
                            "description": "项目id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "sprintId",
                            "in": "query",
                            "description": "冲刺id",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "startTime",
                            "in": "query",
                            "description": "开始时间",
                            "required": False,
                            "type": "string",
                            "format": "date-time"
                        },
                        {
                            "name": "taskCount",
                            "in": "query",
                            "description": "任务数量",
                            "required": False,
                            "type": "integer",
                            "format": "int64"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ItemData«ProjectSprintReportVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/{projectId}/delete": {
                "delete": {
                    "tags": ["文档管理"],
                    "summary": "文档删除",
                    "operationId": "deleteUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "allOnly",
                        "in": "query",
                        "required": False,
                        "type": "boolean"
                    },
                        {
                            "name": "createTime",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "createrId",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "createrName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "createrOnly",
                            "in": "query",
                            "required": False,
                            "type": "boolean"
                        },
                        {
                            "name": "desc",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "docId",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "docUrl",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "fileEnd",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectName",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectOnly",
                            "in": "query",
                            "required": False,
                            "type": "boolean"
                        },
                        {
                            "name": "runtime",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "searchkey",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "title",
                            "in": "query",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/{projectId}/search": {
                "get": {
                    "tags": ["文档管理"],
                    "summary": "查询项目文档",
                    "operationId": "searchInProjectUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "allOnly",
                        "in": "query",
                        "required": False,
                        "type": "boolean"
                    },
                        {
                            "name": "createrOnly",
                            "in": "query",
                            "required": False,
                            "type": "boolean"
                        },
                        {
                            "name": "fileEnd",
                            "in": "query",
                            "description": "文件后缀",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "pageNum",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "projectOnly",
                            "in": "query",
                            "required": False,
                            "type": "boolean"
                        },
                        {
                            "name": "searchkey",
                            "in": "query",
                            "description": "关键字",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "size",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "format": "int32"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/CollectionData«DocVO»"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/{projectId}/upload": {
                "post": {
                    "tags": ["文档管理"],
                    "summary": "文档上传",
                    "operationId": "uploadUsingPOST",
                    "consumes": ["multipart/form-data"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "allOnly",
                        "in": "query",
                        "description": "公开",
                        "required": False,
                        "type": "boolean"
                    },
                        {
                            "name": "createrOnly",
                            "in": "query",
                            "description": "个人可见",
                            "required": False,
                            "type": "boolean"
                        },
                        {
                            "name": "desc",
                            "in": "query",
                            "description": "描述",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "file",
                            "in": "formData",
                            "description": "file",
                            "required": False,
                            "type": "file"
                        },
                        {
                            "name": "fileName",
                            "in": "query",
                            "description": "文件名",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "projectOnly",
                            "in": "query",
                            "description": "项目可见",
                            "required": False,
                            "type": "boolean"
                        },
                        {
                            "name": "title",
                            "in": "query",
                            "description": "标题",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "uploadPath",
                            "in": "query",
                            "description": "文件存放地址",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/{projectId}/users/{userId}/pencent": {
                "get": {
                    "tags": ["项目设置层-项目人员"],
                    "summary": "获取用户项目全时率",
                    "operationId": "getPlateUserPencentUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "projectId",
                        "in": "path",
                        "description": "projectId",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "userId",
                            "in": "path",
                            "description": "userId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/ProjectUserVO"
                                    }
                                }
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/{projectId}/{filePath}/download": {
                "get": {
                    "tags": ["文档管理"],
                    "summary": "文档下载",
                    "operationId": "downloadUsingGET",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "filePath",
                        "in": "path",
                        "description": "filePath",
                        "required": True,
                        "type": "string"
                    },
                        {
                            "name": "projectId",
                            "in": "path",
                            "description": "projectId",
                            "required": True,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK"
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/api/task/{sprintReportId}": {
                "delete": {
                    "tags": ["任务冲刺报告"],
                    "summary": "删除",
                    "operationId": "deleteProjectSprintReportUsingDELETE",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "sprintReportId",
                        "in": "path",
                        "description": "sprintReportId",
                        "required": True,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/error": {
                "get": {
                    "tags": ["basic-error-controller"],
                    "summary": "errorHtml",
                    "operationId": "errorHtmlUsingGET",
                    "produces": ["text/html"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ModelAndView"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "head": {
                    "tags": ["basic-error-controller"],
                    "summary": "errorHtml",
                    "operationId": "errorHtmlUsingHEAD",
                    "consumes": ["application/json"],
                    "produces": ["text/html"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ModelAndView"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["basic-error-controller"],
                    "summary": "errorHtml",
                    "operationId": "errorHtmlUsingPOST",
                    "consumes": ["application/json"],
                    "produces": ["text/html"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ModelAndView"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "put": {
                    "tags": ["basic-error-controller"],
                    "summary": "errorHtml",
                    "operationId": "errorHtmlUsingPUT",
                    "consumes": ["application/json"],
                    "produces": ["text/html"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ModelAndView"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "delete": {
                    "tags": ["basic-error-controller"],
                    "summary": "errorHtml",
                    "operationId": "errorHtmlUsingDELETE",
                    "produces": ["text/html"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ModelAndView"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "options": {
                    "tags": ["basic-error-controller"],
                    "summary": "errorHtml",
                    "operationId": "errorHtmlUsingOPTIONS",
                    "consumes": ["application/json"],
                    "produces": ["text/html"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ModelAndView"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "patch": {
                    "tags": ["basic-error-controller"],
                    "summary": "errorHtml",
                    "operationId": "errorHtmlUsingPATCH",
                    "consumes": ["application/json"],
                    "produces": ["text/html"],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "$ref": "#/definitions/ModelAndView"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            },
            "/fastdfs": {
                "get": {
                    "tags": ["文件上传"],
                    "summary": "download",
                    "operationId": "downloadUsingGET_1",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "fileId",
                        "in": "query",
                        "description": "fileId",
                        "required": False,
                        "type": "string"
                    },
                        {
                            "name": "groupName",
                            "in": "query",
                            "description": "groupName",
                            "required": False,
                            "type": "string"
                        }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "post": {
                    "tags": ["文件上传"],
                    "summary": "upload",
                    "operationId": "uploadUsingPOST_1",
                    "consumes": ["multipart/form-data"],
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "file",
                        "in": "formData",
                        "description": "file",
                        "required": True,
                        "type": "file"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "string",
                                "enum": ["NULL",
                                         "STRING"]
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                },
                "delete": {
                    "tags": ["文件上传"],
                    "summary": "delete",
                    "operationId": "deleteUsingDELETE_1",
                    "produces": ["*/*"],
                    "parameters": [{
                        "name": "file_id",
                        "in": "query",
                        "description": "file_id",
                        "required": False,
                        "type": "string"
                    }],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "schema": {
                                "type": "boolean"
                            }
                        }
                    },
                    "security": [{
                        "token": ["global"]
                    }],
                    "deprecated": False
                }
            }
        },
        "securityDefinitions": {
            "token": {
                "type": "apiKey",
                "name": "token",
                "in": "header"
            }
        },
        "definitions": {
            "AssessIndicatorConfig": {
                "type": "object",
                "properties": {
                    "assessIndicatorId": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "assessIndicatorName": {
                        "type": "string"
                    },
                    "baseScore": {
                        "type": "number"
                    },
                    "createTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "id": {
                        "type": "string"
                    },
                    "initialScore": {
                        "type": "number"
                    },
                    "qualifiedScore": {
                        "type": "number"
                    },
                    "updateTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "userType": {
                        "type": "integer",
                        "format": "int32"
                    }
                },
                "title": "AssessIndicatorConfig"
            },
            "AssessIndicatorConfigVO": {
                "type": "object",
                "properties": {
                    "assessIndicatorId": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "assessIndicatorName": {
                        "type": "string"
                    },
                    "basePoint": {
                        "type": "number"
                    },
                    "baseScore": {
                        "type": "number"
                    },
                    "id": {
                        "type": "string"
                    },
                    "initialScore": {
                        "type": "number"
                    },
                    "qualifiedScore": {
                        "type": "number"
                    },
                    "userType": {
                        "type": "integer",
                        "format": "int32"
                    }
                },
                "title": "AssessIndicatorConfigVO"
            },
            "AssessIndicatorDict": {
                "type": "object",
                "properties": {
                    "assessIndicatorId": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "assessIndicatorName": {
                        "type": "string"
                    },
                    "createTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "id": {
                        "type": "string"
                    },
                    "updateTime": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "AssessIndicatorDict"
            },
            "AssessIndicatorDictVO": {
                "type": "object",
                "properties": {
                    "assessIndicatorId": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "assessIndicatorName": {
                        "type": "string"
                    },
                    "createTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "id": {
                        "type": "string"
                    },
                    "updateTime": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "AssessIndicatorDictVO"
            },
            "AssessItemNoticeVO": {
                "type": "object",
                "properties": {
                    "assessType": {
                        "type": "string"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "defaultScore": {
                        "type": "number"
                    },
                    "executorRole": {
                        "type": "string"
                    },
                    "itemId": {
                        "type": "string"
                    },
                    "itemName": {
                        "type": "string"
                    },
                    "managerId": {
                        "type": "string"
                    },
                    "parentId": {
                        "type": "string"
                    },
                    "parentName": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "AssessItemNoticeVO"
            },
            "AssessItemRecursiveVO": {
                "type": "object",
                "properties": {
                    "assessType": {
                        "type": "string"
                    },
                    "childAssessItem": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/AssessItemRecursiveVO"
                        }
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "defaultScore": {
                        "type": "number"
                    },
                    "executorRole": {
                        "type": "string"
                    },
                    "itemId": {
                        "type": "string"
                    },
                    "itemName": {
                        "type": "string"
                    },
                    "parentId": {
                        "type": "string"
                    },
                    "parentName": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "AssessItemRecursiveVO"
            },
            "AssessItemVO": {
                "type": "object",
                "properties": {
                    "assessType": {
                        "type": "string"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "defaultScore": {
                        "type": "number"
                    },
                    "executorRole": {
                        "type": "string"
                    },
                    "itemId": {
                        "type": "string"
                    },
                    "itemName": {
                        "type": "string"
                    },
                    "parentId": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "AssessItemVO"
            },
            "AssessNoticeItemVO": {
                "type": "object",
                "properties": {
                    "assessItemList": {
                        "type": "array",
                        "description": "考核项集合",
                        "items": {
                            "$ref": "#/definitions/AssessItemNoticeVO"
                        }
                    },
                    "assessNoticeId": {
                        "type": "string",
                        "description": "考核通知id"
                    },
                    "assessStatus": {
                        "type": "integer",
                        "format": "int32",
                        "description": "审核状态"
                    },
                    "assessTimeEnd": {
                        "type": "string",
                        "format": "date-time",
                        "description": "考核截至时间"
                    },
                    "assessTimeStart": {
                        "type": "string",
                        "format": "date-time",
                        "description": "考核开始时间"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time",
                        "description": "创建时间"
                    },
                    "creatorId": {
                        "type": "string",
                        "description": "创建者id"
                    },
                    "description": {
                        "type": "string",
                        "description": "描述"
                    },
                    "executorRole": {
                        "type": "string",
                        "description": "执行角色"
                    },
                    "itemList": {
                        "type": "array",
                        "description": "考核项列表",
                        "items": {
                            "$ref": "#/definitions/NoticeItemVO"
                        }
                    },
                    "noticeName": {
                        "type": "string",
                        "description": "通知名称"
                    },
                    "projectId": {
                        "type": "string",
                        "description": "项目id"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time",
                        "description": "更新时间"
                    },
                    "updaterId": {
                        "type": "string",
                        "description": "更新者id"
                    }
                },
                "title": "AssessNoticeItemVO"
            },
            "AssessNoticeVO": {
                "type": "object",
                "properties": {
                    "assessNoticeId": {
                        "type": "string",
                        "description": "考核通知id"
                    },
                    "assessStatus": {
                        "type": "string",
                        "description": "审核状态"
                    },
                    "assessTimeEnd": {
                        "type": "string",
                        "format": "date-time",
                        "description": "考核截至时间"
                    },
                    "assessTimeStart": {
                        "type": "string",
                        "format": "date-time",
                        "description": "考核开始时间"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time",
                        "description": "创建时间"
                    },
                    "creatorId": {
                        "type": "string",
                        "description": "创建者id"
                    },
                    "creatorName": {
                        "type": "string",
                        "description": "创建者姓名"
                    },
                    "description": {
                        "type": "string",
                        "description": "描述"
                    },
                    "executorRole": {
                        "type": "string",
                        "description": "执行角色"
                    },
                    "itemList": {
                        "type": "array",
                        "description": "考核项列表",
                        "items": {
                            "$ref": "#/definitions/NoticeItemVO"
                        }
                    },
                    "managerName": {
                        "type": "string",
                        "description": "项目经理姓名"
                    },
                    "noticeName": {
                        "type": "string",
                        "description": "通知名称"
                    },
                    "projectName": {
                        "type": "string",
                        "description": "项目名称"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time",
                        "description": "更新时间"
                    },
                    "updaterId": {
                        "type": "string",
                        "description": "更新者id"
                    },
                    "updaterName": {
                        "type": "string",
                        "description": "更新者姓名"
                    }
                },
                "title": "AssessNoticeVO"
            },
            "AssessRecordVO": {
                "type": "object",
                "properties": {
                    "assessNoticeId": {
                        "type": "string"
                    },
                    "assessRecordId": {
                        "type": "string"
                    },
                    "assessType": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "creatorId": {
                        "type": "string"
                    },
                    "creatorName": {
                        "type": "string"
                    },
                    "itemDescription": {
                        "type": "string"
                    },
                    "itemId": {
                        "type": "string"
                    },
                    "itemName": {
                        "type": "string"
                    },
                    "itemScore": {
                        "type": "number"
                    },
                    "managerId": {
                        "type": "string"
                    },
                    "managerName": {
                        "type": "string"
                    },
                    "parentName": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    }
                },
                "title": "AssessRecordVO"
            },
            "Assessment": {
                "type": "object",
                "properties": {
                    "createBy": {
                        "type": "string",
                        "description": "评价人"
                    },
                    "createTime": {
                        "type": "string",
                        "format": "date-time",
                        "description": "创建时间"
                    },
                    "creatorId": {
                        "type": "string",
                        "description": "评价人id"
                    },
                    "projectId": {
                        "type": "string",
                        "description": "项目ID"
                    },
                    "score": {
                        "type": "string",
                        "description": "分数"
                    },
                    "scoreId": {
                        "type": "string",
                        "description": "分数ID"
                    }
                },
                "title": "Assessment"
            },
            "AssessmentVO": {
                "type": "object",
                "properties": {
                    "createBy": {
                        "type": "string",
                        "description": "评价人"
                    },
                    "createTime": {
                        "type": "string",
                        "format": "date-time",
                        "description": "创建时间"
                    },
                    "creatorId": {
                        "type": "string",
                        "description": "评价人id"
                    },
                    "projectId": {
                        "type": "string",
                        "description": "项目ID"
                    },
                    "questions": {
                        "type": "array",
                        "description": "问题列表",
                        "items": {
                            "type": "object"
                        }
                    },
                    "score": {
                        "type": "array",
                        "description": "分数",
                        "items": {
                            "type": "object"
                        }
                    },
                    "scoreId": {
                        "type": "string",
                        "description": "分数ID"
                    },
                    "type": {
                        "type": "integer",
                        "format": "int32",
                        "description": "类型（0为问卷，1为答案列表）"
                    }
                },
                "title": "AssessmentVO"
            },
            "BaseConfigVO": {
                "type": "object",
                "properties": {
                    "addedScore": {
                        "type": "number"
                    },
                    "assessProportion": {
                        "type": "number"
                    },
                    "baseCfgId": {
                        "type": "string"
                    },
                    "flowerScore": {
                        "type": "number"
                    },
                    "fullDayPoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "punishScore": {
                        "type": "number"
                    },
                    "shareScore": {
                        "type": "number"
                    }
                },
                "title": "BaseConfigVO"
            },
            "CollectionData«AssessIndicatorConfigVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/AssessIndicatorConfigVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«AssessIndicatorConfigVO»"
            },
            "CollectionData«AssessIndicatorDictVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/AssessIndicatorDictVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«AssessIndicatorDictVO»"
            },
            "CollectionData«AssessItemRecursiveVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/AssessItemRecursiveVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«AssessItemRecursiveVO»"
            },
            "CollectionData«AssessNoticeVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/AssessNoticeVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«AssessNoticeVO»"
            },
            "CollectionData«AssessRecordVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/AssessRecordVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«AssessRecordVO»"
            },
            "CollectionData«DealTaskVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/DealTaskVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«DealTaskVO»"
            },
            "CollectionData«DealVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/DealVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«DealVO»"
            },
            "CollectionData«DepartmentVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/DepartmentVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«DepartmentVO»"
            },
            "CollectionData«Department»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/Department"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«Department»"
            },
            "CollectionData«DocVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/DocVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«DocVO»"
            },
            "CollectionData«LevelBasePoint»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/LevelBasePoint"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«LevelBasePoint»"
            },
            "CollectionData«ManagerReportVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ManagerReportVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ManagerReportVO»"
            },
            "CollectionData«Map«string,int»»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/Map«string,int»"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«Map«string,int»»"
            },
            "CollectionData«MenuFunction»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/MenuFunction"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«MenuFunction»"
            },
            "CollectionData«Pair«string,List«AssessRecordVO»»»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/Pair«string,List«AssessRecordVO»»"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«Pair«string,List«AssessRecordVO»»»"
            },
            "CollectionData«Pair«string,List«NoticeItemVO»»»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/Pair«string,List«NoticeItemVO»»"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«Pair«string,List«NoticeItemVO»»»"
            },
            "CollectionData«PersonalProjectWorkVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/PersonalProjectWorkVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«PersonalProjectWorkVO»"
            },
            "CollectionData«PersonalTypeVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/PersonalTypeVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«PersonalTypeVO»"
            },
            "CollectionData«ProjectAndRecruitVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectAndRecruitVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectAndRecruitVO»"
            },
            "CollectionData«ProjectApplyApproveVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectApplyApproveVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectApplyApproveVO»"
            },
            "CollectionData«ProjectApplyVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectApplyVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectApplyVO»"
            },
            "CollectionData«ProjectArchiveTaskVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectArchiveTaskVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectArchiveTaskVO»"
            },
            "CollectionData«ProjectManagerVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectManagerVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectManagerVO»"
            },
            "CollectionData«ProjectMemberReportVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectMemberReportVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectMemberReportVO»"
            },
            "CollectionData«ProjectPlanMemberVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectPlanMemberVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectPlanMemberVO»"
            },
            "CollectionData«ProjectPlanVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectPlanVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectPlanVO»"
            },
            "CollectionData«ProjectRecruitVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectRecruitVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectRecruitVO»"
            },
            "CollectionData«ProjectRoleVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectRoleVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectRoleVO»"
            },
            "CollectionData«ProjectSprintVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectSprintVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectSprintVO»"
            },
            "CollectionData«ProjectTaskCountAndSumVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectTaskCountAndSumVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectTaskCountAndSumVO»"
            },
            "CollectionData«ProjectTaskPriorityVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectTaskPriorityVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectTaskPriorityVO»"
            },
            "CollectionData«ProjectTaskReplyVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectTaskReplyVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectTaskReplyVO»"
            },
            "CollectionData«ProjectTaskStatusVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectTaskStatusVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectTaskStatusVO»"
            },
            "CollectionData«ProjectTaskTypeVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectTaskTypeVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectTaskTypeVO»"
            },
            "CollectionData«ProjectTaskVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectTaskVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectTaskVO»"
            },
            "CollectionData«ProjectVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ProjectVO»"
            },
            "CollectionData«ReportVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ReportVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«ReportVO»"
            },
            "CollectionData«Role»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/Role"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«Role»"
            },
            "CollectionData«SimpleMenuResp»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/SimpleMenuResp"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«SimpleMenuResp»"
            },
            "CollectionData«StandardConfigVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/StandardConfigVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«StandardConfigVO»"
            },
            "CollectionData«SystemTempPriorityVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/SystemTempPriorityVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«SystemTempPriorityVO»"
            },
            "CollectionData«SystemTempRoleVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/SystemTempRoleVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«SystemTempRoleVO»"
            },
            "CollectionData«SystemTempStatusVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/SystemTempStatusVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«SystemTempStatusVO»"
            },
            "CollectionData«SystemTempTypeVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/SystemTempTypeVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«SystemTempTypeVO»"
            },
            "CollectionData«SystemTempVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/SystemTempVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«SystemTempVO»"
            },
            "CollectionData«UserScoreReportVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/UserScoreReportVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«UserScoreReportVO»"
            },
            "CollectionData«UserTaskVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/UserTaskVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«UserTaskVO»"
            },
            "CollectionData«User»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/User"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«User»"
            },
            "CollectionData«WorkerVO»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/WorkerVO"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«WorkerVO»"
            },
            "CollectionData«string»": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "CollectionData«string»"
            },
            "DealTaskVO": {
                "type": "object",
                "properties": {
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "dealId": {
                        "type": "string"
                    },
                    "dealType": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "remark": {
                        "type": "string"
                    },
                    "score": {
                        "type": "number"
                    },
                    "taskId": {
                        "type": "string"
                    },
                    "title": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "userId": {
                        "type": "string"
                    },
                    "userName": {
                        "type": "string"
                    }
                },
                "title": "DealTaskVO"
            },
            "DealVO": {
                "type": "object",
                "properties": {
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "dealId": {
                        "type": "string"
                    },
                    "dealType": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "remark": {
                        "type": "string"
                    },
                    "score": {
                        "type": "number"
                    },
                    "taskId": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "userId": {
                        "type": "string"
                    }
                },
                "title": "DealVO"
            },
            "Department": {
                "type": "object",
                "properties": {
                    "createBy": {
                        "type": "string"
                    },
                    "defaultTag": {
                        "type": "string"
                    },
                    "departmentId": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "flag1": {
                        "type": "string"
                    },
                    "flag2": {
                        "type": "string"
                    },
                    "flag3": {
                        "type": "string"
                    },
                    "flag4": {
                        "type": "string"
                    },
                    "flag5": {
                        "type": "string"
                    },
                    "flag6": {
                        "type": "string"
                    },
                    "level": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "name": {
                        "type": "string"
                    },
                    "parentId": {
                        "type": "string"
                    },
                    "parentName": {
                        "type": "string"
                    },
                    "remark": {
                        "type": "string"
                    },
                    "sortNumber": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "status": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "systemId": {
                        "type": "string"
                    },
                    "type": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "updateBy": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "Department"
            },
            "DepartmentVO": {
                "type": "object",
                "properties": {
                    "createBy": {
                        "type": "string"
                    },
                    "departmentChildren": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/DepartmentVO"
                        }
                    },
                    "departmentId": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "level": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "modifyDate": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "name": {
                        "type": "string"
                    },
                    "parentId": {
                        "type": "string"
                    },
                    "parentName": {
                        "type": "string"
                    },
                    "remark": {
                        "type": "string"
                    },
                    "sortNumber": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "status": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "updateBy": {
                        "type": "string"
                    }
                },
                "title": "DepartmentVO"
            },
            "DocVO": {
                "type": "object",
                "required": ["allOnly",
                             "createrOnly",
                             "projectOnly"],
                "properties": {
                    "allOnly": {
                        "type": "boolean"
                    },
                    "createTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "createrId": {
                        "type": "string"
                    },
                    "createrName": {
                        "type": "string"
                    },
                    "createrOnly": {
                        "type": "boolean"
                    },
                    "desc": {
                        "type": "string"
                    },
                    "docId": {
                        "type": "string"
                    },
                    "docUrl": {
                        "type": "string"
                    },
                    "fileEnd": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "projectOnly": {
                        "type": "boolean"
                    },
                    "title": {
                        "type": "string"
                    }
                },
                "title": "DocVO"
            },
            "ItemData«AssessIndicatorConfig»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/AssessIndicatorConfig"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«AssessIndicatorConfig»"
            },
            "ItemData«AssessIndicatorDictVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/AssessIndicatorDictVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«AssessIndicatorDictVO»"
            },
            "ItemData«AssessIndicatorDict»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/AssessIndicatorDict"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«AssessIndicatorDict»"
            },
            "ItemData«AssessItemVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/AssessItemVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«AssessItemVO»"
            },
            "ItemData«AssessNoticeItemVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/AssessNoticeItemVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«AssessNoticeItemVO»"
            },
            "ItemData«AssessNoticeVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/AssessNoticeVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«AssessNoticeVO»"
            },
            "ItemData«Department»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/Department"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«Department»"
            },
            "ItemData«LevelBasePoint»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/LevelBasePoint"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«LevelBasePoint»"
            },
            "ItemData«Map«string,object»»": {
                "type": "object",
                "properties": {
                    "item": {
                        "type": "object"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«Map«string,object»»"
            },
            "ItemData«MenuFunction»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/MenuFunction"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«MenuFunction»"
            },
            "ItemData«ProjectAndRecruitVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/ProjectAndRecruitVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«ProjectAndRecruitVO»"
            },
            "ItemData«ProjectApplyApproveVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/ProjectApplyApproveVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«ProjectApplyApproveVO»"
            },
            "ItemData«ProjectApplyVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/ProjectApplyVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«ProjectApplyVO»"
            },
            "ItemData«ProjectPlanVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/ProjectPlanVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«ProjectPlanVO»"
            },
            "ItemData«ProjectRecruitVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/ProjectRecruitVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«ProjectRecruitVO»"
            },
            "ItemData«ProjectSprintMemberReportVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/ProjectSprintMemberReportVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«ProjectSprintMemberReportVO»"
            },
            "ItemData«ProjectSprintReportVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/ProjectSprintReportVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«ProjectSprintReportVO»"
            },
            "ItemData«ProjectTaskVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/ProjectTaskVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«ProjectTaskVO»"
            },
            "ItemData«ProjectVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/ProjectVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«ProjectVO»"
            },
            "ItemData«Role»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/Role"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«Role»"
            },
            "ItemData«UserVO»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/UserVO"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«UserVO»"
            },
            "ItemData«User»": {
                "type": "object",
                "properties": {
                    "item": {
                        "$ref": "#/definitions/User"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«User»"
            },
            "ItemData«string»": {
                "type": "object",
                "properties": {
                    "item": {
                        "type": "string"
                    },
                    "meta": {
                        "type": "object"
                    }
                },
                "title": "ItemData«string»"
            },
            "LevelBasePoint": {
                "type": "object",
                "properties": {
                    "basePoint": {
                        "type": "number"
                    },
                    "createTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "evaluateQualifiedScore": {
                        "type": "number"
                    },
                    "id": {
                        "type": "string"
                    },
                    "levelId": {
                        "type": "string"
                    },
                    "levelName": {
                        "type": "string"
                    },
                    "updateTime": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "LevelBasePoint"
            },
            "ManagerReportVO": {
                "type": "object",
                "properties": {
                    "assessScore": {
                        "type": "number"
                    },
                    "createTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "managerId": {
                        "type": "string"
                    },
                    "managerName": {
                        "type": "string"
                    },
                    "managerReportId": {
                        "type": "string"
                    },
                    "personalScore": {
                        "type": "number"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "projectScore": {
                        "type": "number"
                    },
                    "sumScore": {
                        "type": "number"
                    }
                },
                "title": "ManagerReportVO"
            },
            "Map«string,int»": {
                "type": "object",
                "title": "Map«string,int»",
                "additionalProperties": {
                    "$ref": "#/definitions/Integer"
                }
            },
            "MenuFunction": {
                "type": "object",
                "properties": {
                    "component": {
                        "type": "string"
                    },
                    "createBy": {
                        "type": "string"
                    },
                    "desciption": {
                        "type": "string"
                    },
                    "flag1": {
                        "type": "string"
                    },
                    "flag2": {
                        "type": "string"
                    },
                    "flag3": {
                        "type": "string"
                    },
                    "flag4": {
                        "type": "string"
                    },
                    "flag5": {
                        "type": "string"
                    },
                    "flag6": {
                        "type": "string"
                    },
                    "menuId": {
                        "type": "string"
                    },
                    "menuLevel": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "name": {
                        "type": "string"
                    },
                    "parentId": {
                        "type": "string"
                    },
                    "remark": {
                        "type": "string"
                    },
                    "requestMode": {
                        "type": "string"
                    },
                    "shortCutIcon": {
                        "type": "string"
                    },
                    "sortNumber": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "systemId": {
                        "type": "string"
                    },
                    "type": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "updateBy": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "url": {
                        "type": "string"
                    },
                    "visible": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "webPath": {
                        "type": "string"
                    }
                },
                "title": "MenuFunction"
            },
            "ModelAndView": {
                "type": "object",
                "properties": {
                    "empty": {
                        "type": "boolean"
                    },
                    "model": {
                        "type": "object"
                    },
                    "modelMap": {
                        "type": "object",
                        "additionalProperties": {
                            "type": "object"
                        }
                    },
                    "reference": {
                        "type": "boolean"
                    },
                    "status": {
                        "type": "string",
                        "enum": ["100 CONTINUE",
                                 "101 SWITCHING_PROTOCOLS",
                                 "102 PROCESSING",
                                 "103 CHECKPOINT",
                                 "200 OK",
                                 "201 CREATED",
                                 "202 ACCEPTED",
                                 "203 NON_AUTHORITATIVE_INFORMATION",
                                 "204 NO_CONTENT",
                                 "205 RESET_CONTENT",
                                 "206 PARTIAL_CONTENT",
                                 "207 MULTI_STATUS",
                                 "208 ALREADY_REPORTED",
                                 "226 IM_USED",
                                 "300 MULTIPLE_CHOICES",
                                 "301 MOVED_PERMANENTLY",
                                 "302 FOUND",
                                 "302 MOVED_TEMPORARILY",
                                 "303 SEE_OTHER",
                                 "304 NOT_MODIFIED",
                                 "305 USE_PROXY",
                                 "307 TEMPORARY_REDIRECT",
                                 "308 PERMANENT_REDIRECT",
                                 "400 BAD_REQUEST",
                                 "401 UNAUTHORIZED",
                                 "402 PAYMENT_REQUIRED",
                                 "403 FORBIDDEN",
                                 "404 NOT_FOUND",
                                 "405 METHOD_NOT_ALLOWED",
                                 "406 NOT_ACCEPTABLE",
                                 "407 PROXY_AUTHENTICATION_REQUIRED",
                                 "408 REQUEST_TIMEOUT",
                                 "409 CONFLICT",
                                 "410 GONE",
                                 "411 LENGTH_REQUIRED",
                                 "412 PRECONDITION_FAILED",
                                 "413 PAYLOAD_TOO_LARGE",
                                 "413 REQUEST_ENTITY_TOO_LARGE",
                                 "414 URI_TOO_LONG",
                                 "414 REQUEST_URI_TOO_LONG",
                                 "415 UNSUPPORTED_MEDIA_TYPE",
                                 "416 REQUESTED_RANGE_NOT_SATISFIABLE",
                                 "417 EXPECTATION_FAILED",
                                 "418 I_AM_A_TEAPOT",
                                 "419 INSUFFICIENT_SPACE_ON_RESOURCE",
                                 "420 METHOD_FAILURE",
                                 "421 DESTINATION_LOCKED",
                                 "422 UNPROCESSABLE_ENTITY",
                                 "423 LOCKED",
                                 "424 FAILED_DEPENDENCY",
                                 "425 TOO_EARLY",
                                 "426 UPGRADE_REQUIRED",
                                 "428 PRECONDITION_REQUIRED",
                                 "429 TOO_MANY_REQUESTS",
                                 "431 REQUEST_HEADER_FIELDS_TOO_LARGE",
                                 "451 UNAVAILABLE_FOR_LEGAL_REASONS",
                                 "500 INTERNAL_SERVER_ERROR",
                                 "501 NOT_IMPLEMENTED",
                                 "502 BAD_GATEWAY",
                                 "503 SERVICE_UNAVAILABLE",
                                 "504 GATEWAY_TIMEOUT",
                                 "505 HTTP_VERSION_NOT_SUPPORTED",
                                 "506 VARIANT_ALSO_NEGOTIATES",
                                 "507 INSUFFICIENT_STORAGE",
                                 "508 LOOP_DETECTED",
                                 "509 BANDWIDTH_LIMIT_EXCEEDED",
                                 "510 NOT_EXTENDED",
                                 "511 NETWORK_AUTHENTICATION_REQUIRED"]
                    },
                    "view": {
                        "$ref": "#/definitions/View"
                    },
                    "viewName": {
                        "type": "string"
                    }
                },
                "title": "ModelAndView"
            },
            "NoticeItemVO": {
                "type": "object",
                "properties": {
                    "assessNoticeId": {
                        "type": "string"
                    },
                    "assessType": {
                        "type": "string"
                    },
                    "changeMessage": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    },
                    "itemDescription": {
                        "type": "string"
                    },
                    "itemId": {
                        "type": "string"
                    },
                    "itemName": {
                        "type": "string"
                    },
                    "itemScore": {
                        "type": "number"
                    },
                    "managerId": {
                        "type": "string",
                        "description": "项目经理id"
                    },
                    "managerName": {
                        "type": "string",
                        "description": "项目经理姓名"
                    },
                    "noticeItemId": {
                        "type": "string"
                    },
                    "noticeName": {
                        "type": "string"
                    },
                    "noticeType": {
                        "type": "string"
                    },
                    "parentId": {
                        "type": "string"
                    },
                    "parentName": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "readFlag": {
                        "type": "string"
                    }
                },
                "title": "NoticeItemVO"
            },
            "Pair«string,List«AssessRecordVO»»": {
                "type": "object",
                "required": ["first",
                             "second"],
                "properties": {
                    "first": {
                        "type": "string"
                    },
                    "second": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/AssessRecordVO"
                        }
                    }
                },
                "title": "Pair«string,List«AssessRecordVO»»"
            },
            "Pair«string,List«NoticeItemVO»»": {
                "type": "object",
                "required": ["first",
                             "second"],
                "properties": {
                    "first": {
                        "type": "string"
                    },
                    "second": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/NoticeItemVO"
                        }
                    }
                },
                "title": "Pair«string,List«NoticeItemVO»»"
            },
            "PersonalProjectWorkVO": {
                "type": "object",
                "properties": {
                    "actualPoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "addedScore": {
                        "type": "number"
                    },
                    "archivePoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "bugCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "bugPoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "finishTaskCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "finishTaskPoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "flowerScore": {
                        "type": "number"
                    },
                    "leftJson": {
                        "type": "string"
                    },
                    "percent": {
                        "type": "number"
                    },
                    "priceCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "pricePoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "punishScore": {
                        "type": "number"
                    },
                    "rank": {
                        "type": "number"
                    },
                    "reportId": {
                        "type": "string"
                    },
                    "reportName": {
                        "type": "string"
                    },
                    "reportScoreList": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ReportScoreVO"
                        }
                    },
                    "taskCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "taskPoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "unfinishTaskCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "unfinishTaskPoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "userId": {
                        "type": "string"
                    },
                    "userName": {
                        "type": "string"
                    }
                },
                "title": "PersonalProjectWorkVO"
            },
            "PersonalTypeVO": {
                "type": "object",
                "required": ["typeId",
                             "typeName"],
                "properties": {
                    "typeId": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "typeName": {
                        "type": "string"
                    }
                },
                "title": "PersonalTypeVO"
            },
            "ProjectAndRecruitVO": {
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string"
                    },
                    "endTime": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "projectRecruit": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectRecruit"
                        }
                    },
                    "startTime": {
                        "type": "string"
                    }
                },
                "title": "ProjectAndRecruitVO"
            },
            "ProjectApplyApproveVO": {
                "type": "object",
                "properties": {
                    "applyId": {
                        "type": "string"
                    },
                    "applyType": {
                        "type": "string"
                    },
                    "applyUserDescription": {
                        "type": "string"
                    },
                    "applyUserId": {
                        "type": "string"
                    },
                    "applyUserName": {
                        "type": "string"
                    },
                    "approveDescription": {
                        "type": "string"
                    },
                    "approveId": {
                        "type": "string"
                    },
                    "approveStatus": {
                        "type": "string"
                    },
                    "approveTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "approveType": {
                        "type": "string"
                    },
                    "approveUserId": {
                        "type": "string"
                    },
                    "approveUserName": {
                        "type": "string"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "postDescription": {
                        "type": "string"
                    },
                    "postJobShare": {
                        "type": "string"
                    },
                    "postName": {
                        "type": "string"
                    },
                    "postType": {
                        "type": "string"
                    },
                    "proRoleId": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "roleType": {
                        "type": "string"
                    }
                },
                "title": "ProjectApplyApproveVO"
            },
            "ProjectApplyVO": {
                "type": "object",
                "properties": {
                    "applyId": {
                        "type": "string"
                    },
                    "applyStatus": {
                        "type": "string"
                    },
                    "applyType": {
                        "type": "string"
                    },
                    "applyUserDescription": {
                        "type": "string"
                    },
                    "applyUserId": {
                        "type": "string"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "postDescription": {
                        "type": "string"
                    },
                    "postJobShare": {
                        "type": "string"
                    },
                    "postName": {
                        "type": "string"
                    },
                    "postType": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "recruitId": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "ProjectApplyVO"
            },
            "ProjectArchiveTaskVO": {
                "type": "object",
                "properties": {
                    "activePoints": {
                        "type": "number"
                    },
                    "archiveAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "attr": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "executorId": {
                        "type": "string"
                    },
                    "points": {
                        "type": "number"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "remark": {
                        "type": "string"
                    },
                    "score": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "scoreId": {
                        "type": "string"
                    },
                    "scoredAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "taskId": {
                        "type": "string"
                    },
                    "taskTitle": {
                        "type": "string"
                    }
                },
                "title": "ProjectArchiveTaskVO"
            },
            "ProjectManagerVO": {
                "type": "object",
                "properties": {
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "userId": {
                        "type": "string"
                    },
                    "userName": {
                        "type": "string"
                    }
                },
                "title": "ProjectManagerVO"
            },
            "ProjectMemberReportVO": {
                "type": "object",
                "properties": {
                    "attScore": {
                        "type": "number",
                        "format": "double"
                    },
                    "finishCount": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "finishPoints": {
                        "type": "number",
                        "format": "double"
                    },
                    "finishedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "pointTotal": {
                        "type": "number",
                        "format": "double"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "remark": {
                        "type": "string"
                    },
                    "score": {
                        "type": "number",
                        "format": "double"
                    },
                    "serial": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "sprintId": {
                        "type": "string"
                    },
                    "startedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "taskCount": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "userId": {
                        "type": "string"
                    }
                },
                "title": "ProjectMemberReportVO"
            },
            "ProjectPlanMemberVO": {
                "type": "object",
                "required": ["taskList"],
                "properties": {
                    "memberId": {
                        "type": "string"
                    },
                    "taskList": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectTaskVO"
                        }
                    }
                },
                "title": "ProjectPlanMemberVO"
            },
            "ProjectPlanVO": {
                "type": "object",
                "properties": {
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "createdBy": {
                        "type": "string"
                    },
                    "desc": {
                        "type": "string"
                    },
                    "endTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "name": {
                        "type": "string"
                    },
                    "planId": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "startTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "status": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "ProjectPlanVO"
            },
            "ProjectRecruit": {
                "type": "object",
                "properties": {
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "endTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "inPlaceSum": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "openFlag": {
                        "type": "string"
                    },
                    "postDescription": {
                        "type": "string"
                    },
                    "postJobShare": {
                        "type": "number"
                    },
                    "postName": {
                        "type": "string"
                    },
                    "postSum": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "postType": {
                        "type": "string"
                    },
                    "proRoleId": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "recruitId": {
                        "type": "string"
                    },
                    "startTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "ProjectRecruit"
            },
            "ProjectRecruitVO": {
                "type": "object",
                "properties": {
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "endTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "inPlaceSum": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "openFlag": {
                        "type": "string"
                    },
                    "postDescription": {
                        "type": "string"
                    },
                    "postJobShare": {
                        "type": "number"
                    },
                    "postName": {
                        "type": "string"
                    },
                    "postSum": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "postType": {
                        "type": "string"
                    },
                    "proRoleId": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "recruitId": {
                        "type": "string"
                    },
                    "startTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "ProjectRecruitVO"
            },
            "ProjectRoleVO": {
                "type": "object",
                "properties": {
                    "cancelSprint": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "createSprint": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "createTask": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "manage": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "proRoleId": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "roleLogoType": {
                        "type": "string"
                    },
                    "roleName": {
                        "type": "string"
                    },
                    "updateTask": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "updatedSprint": {
                        "type": "integer",
                        "format": "int32"
                    }
                },
                "title": "ProjectRoleVO"
            },
            "ProjectSprintMemberReportVO": {
                "type": "object",
                "properties": {
                    "attScore": {
                        "type": "number",
                        "format": "double"
                    },
                    "finishCount": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "finishPoints": {
                        "type": "number",
                        "format": "double"
                    },
                    "memberReportId": {
                        "type": "string"
                    },
                    "month": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "pointTotal": {
                        "type": "number",
                        "format": "double"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "remark": {
                        "type": "string"
                    },
                    "score": {
                        "type": "number",
                        "format": "double"
                    },
                    "sprintId": {
                        "type": "string"
                    },
                    "taskCount": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "userId": {
                        "type": "string"
                    },
                    "week": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "year": {
                        "type": "integer",
                        "format": "int64"
                    }
                },
                "title": "ProjectSprintMemberReportVO"
            },
            "ProjectSprintReportVO": {
                "type": "object",
                "properties": {
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "endTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "finishPoints": {
                        "type": "number",
                        "format": "double"
                    },
                    "finishTask": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "memberCount": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "pointTotal": {
                        "type": "number",
                        "format": "double"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "sprintId": {
                        "type": "string"
                    },
                    "sprintReportId": {
                        "type": "string"
                    },
                    "startTime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "taskCount": {
                        "type": "integer",
                        "format": "int64"
                    }
                },
                "title": "ProjectSprintReportVO"
            },
            "ProjectSprintVO": {
                "type": "object",
                "properties": {
                    "finishedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "serial": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "sprintId": {
                        "type": "string"
                    },
                    "sprintType": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "startedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "status": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "taskCount": {
                        "type": "integer",
                        "format": "int32"
                    }
                },
                "title": "ProjectSprintVO"
            },
            "ProjectTaskCountAndSumSimpleVO": {
                "type": "object",
                "properties": {
                    "pointSum": {
                        "type": "number",
                        "format": "double"
                    },
                    "taskCount": {
                        "type": "integer",
                        "format": "int32"
                    }
                },
                "title": "ProjectTaskCountAndSumSimpleVO"
            },
            "ProjectTaskCountAndSumStatusVO": {
                "type": "object",
                "properties": {
                    "pointSum": {
                        "type": "number",
                        "format": "double"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "show": {
                        "type": "boolean"
                    },
                    "statusColor": {
                        "type": "string"
                    },
                    "statusName": {
                        "type": "string"
                    },
                    "taskCount": {
                        "type": "integer",
                        "format": "int32"
                    }
                },
                "title": "ProjectTaskCountAndSumStatusVO"
            },
            "ProjectTaskCountAndSumVO": {
                "type": "object",
                "properties": {
                    "finishCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "finishSum": {
                        "type": "number",
                        "format": "double"
                    },
                    "percent": {
                        "type": "number"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "roleName": {
                        "type": "string"
                    },
                    "unfinishCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "unfinishSum": {
                        "type": "number",
                        "format": "double"
                    }
                },
                "title": "ProjectTaskCountAndSumVO"
            },
            "ProjectTaskIndexVO": {
                "type": "object",
                "properties": {
                    "finishTaskCountAndSumSimple": {
                        "$ref": "#/definitions/ProjectTaskCountAndSumSimpleVO"
                    },
                    "taskCountAndSumStatus": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectTaskCountAndSumStatusVO"
                        }
                    },
                    "unfinishTaskCountAndSumSimple": {
                        "$ref": "#/definitions/ProjectTaskCountAndSumSimpleVO"
                    },
                    "userDealList": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectUserDealVO"
                        }
                    },
                    "userTaskCountAndSumStatus": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectTaskUserStatusVO"
                        }
                    }
                },
                "title": "ProjectTaskIndexVO"
            },
            "ProjectTaskPriorityVO": {
                "type": "object",
                "properties": {
                    "defaultMark": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "priorityColor": {
                        "type": "string"
                    },
                    "priorityName": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "taskPriorityId": {
                        "type": "string"
                    }
                },
                "title": "ProjectTaskPriorityVO"
            },
            "ProjectTaskReplyVO": {
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "oratorId": {
                        "type": "string"
                    },
                    "replyId": {
                        "type": "string"
                    },
                    "taskId": {
                        "type": "string"
                    }
                },
                "title": "ProjectTaskReplyVO"
            },
            "ProjectTaskStatusVO": {
                "type": "object",
                "properties": {
                    "bugFlag": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "serial": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "statusColor": {
                        "type": "string"
                    },
                    "statusName": {
                        "type": "string"
                    },
                    "statusType": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "taskStatusId": {
                        "type": "string"
                    }
                },
                "title": "ProjectTaskStatusVO"
            },
            "ProjectTaskTypeVO": {
                "type": "object",
                "properties": {
                    "projectId": {
                        "type": "string"
                    },
                    "taskTypeId": {
                        "type": "string"
                    },
                    "typeLogo": {
                        "type": "string"
                    },
                    "typeName": {
                        "type": "string"
                    }
                },
                "title": "ProjectTaskTypeVO"
            },
            "ProjectTaskUserStatusVO": {
                "type": "object",
                "properties": {
                    "operatorNo": {
                        "type": "string"
                    },
                    "taskCountAndSumStatus": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ProjectTaskCountAndSumStatusVO"
                        }
                    },
                    "userId": {
                        "type": "string"
                    },
                    "userName": {
                        "type": "string"
                    }
                },
                "title": "ProjectTaskUserStatusVO"
            },
            "ProjectTaskVO": {
                "type": "object",
                "properties": {
                    "archive": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "broTaskId": {
                        "type": "string"
                    },
                    "bugStatusId": {
                        "type": "string"
                    },
                    "countedPoints": {
                        "type": "number",
                        "format": "double"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "creatorId": {
                        "type": "string"
                    },
                    "deadLine": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "dealId": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "executorId": {
                        "type": "string"
                    },
                    "finishedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "parTaskId": {
                        "type": "string"
                    },
                    "planId": {
                        "type": "string"
                    },
                    "points": {
                        "type": "number",
                        "format": "double"
                    },
                    "priceFlag": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "priorityId": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "sprintId": {
                        "type": "string"
                    },
                    "startedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "statusId": {
                        "type": "string"
                    },
                    "taskGetDateLine": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "taskId": {
                        "type": "string"
                    },
                    "title": {
                        "type": "string"
                    },
                    "typeId": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "ProjectTaskVO"
            },
            "ProjectUserDealVO": {
                "type": "object",
                "properties": {
                    "dealCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "userId": {
                        "type": "string"
                    },
                    "userName": {
                        "type": "string"
                    }
                },
                "title": "ProjectUserDealVO"
            },
            "ProjectUserVO": {
                "type": "object",
                "properties": {
                    "overdueTasks": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "percent": {
                        "type": "number"
                    },
                    "proRoleId": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "roleName": {
                        "type": "string"
                    },
                    "userId": {
                        "type": "string"
                    }
                },
                "title": "ProjectUserVO"
            },
            "ProjectVO": {
                "type": "object",
                "properties": {
                    "archive": {
                        "type": "integer",
                        "format": "int32",
                        "description": "归档标记"
                    },
                    "assessFlag": {
                        "type": "string",
                        "description": "是否纳入考核标志,0:不纳入,1:纳入"
                    },
                    "creatorId": {
                        "type": "string",
                        "description": "创建者id"
                    },
                    "creatorName": {
                        "type": "string",
                        "description": "创建者姓名"
                    },
                    "description": {
                        "type": "string",
                        "description": "项目描述"
                    },
                    "disabled": {
                        "type": "integer",
                        "format": "int32",
                        "description": "终止标记"
                    },
                    "endTime": {
                        "type": "string",
                        "format": "date-time",
                        "description": "结束时间"
                    },
                    "logo": {
                        "type": "string",
                        "description": "项目logo"
                    },
                    "projectId": {
                        "type": "string",
                        "description": "项目id"
                    },
                    "projectName": {
                        "type": "string",
                        "description": "项目名称"
                    },
                    "sprintIndex": {
                        "type": "integer",
                        "format": "int32",
                        "description": "当前冲刺序列"
                    },
                    "startTime": {
                        "type": "string",
                        "format": "date-time",
                        "description": "开始时间"
                    }
                },
                "title": "ProjectVO"
            },
            "ProjectWebHookVO": {
                "type": "object",
                "properties": {
                    "projectId": {
                        "type": "string"
                    },
                    "triggerCancel": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "triggerCreate": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "triggerFinished": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "triggerUpdate": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "webAccess": {
                        "type": "string"
                    },
                    "webSecret": {
                        "type": "string"
                    },
                    "webUrl": {
                        "type": "string"
                    }
                },
                "title": "ProjectWebHookVO"
            },
            "ReportScoreVO": {
                "type": "object",
                "properties": {
                    "indicatorConfigId": {
                        "type": "string"
                    },
                    "indicatorConfigName": {
                        "type": "string"
                    },
                    "overScore": {
                        "type": "number"
                    },
                    "qualified": {
                        "type": "string"
                    },
                    "qualifiedScore": {
                        "type": "number"
                    },
                    "reportId": {
                        "type": "string"
                    },
                    "reportScoreId": {
                        "type": "string"
                    },
                    "score": {
                        "type": "number"
                    }
                },
                "title": "ReportScoreVO"
            },
            "ReportVO": {
                "type": "object",
                "required": ["addedScore",
                             "flowerScore",
                             "kpiPoints",
                             "overScoreSum",
                             "punishScore",
                             "score"],
                "properties": {
                    "actualPoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "addedScore": {
                        "type": "number"
                    },
                    "archivePoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "bugCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "bugPoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "finishTaskCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "finishTaskPoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "flowerScore": {
                        "type": "number"
                    },
                    "kpiPoints": {
                        "type": "number"
                    },
                    "leftJson": {
                        "type": "string"
                    },
                    "overScoreSum": {
                        "type": "number"
                    },
                    "percent": {
                        "type": "number"
                    },
                    "priceCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "pricePoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "punishScore": {
                        "type": "number"
                    },
                    "rank": {
                        "type": "number"
                    },
                    "reportId": {
                        "type": "string"
                    },
                    "reportName": {
                        "type": "string"
                    },
                    "score": {
                        "type": "number"
                    },
                    "scoreList": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ReportScoreVO"
                        }
                    },
                    "taskCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "taskPoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "unfinishTaskCount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "unfinishTaskPoints": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "userId": {
                        "type": "string"
                    },
                    "userName": {
                        "type": "string"
                    }
                },
                "title": "ReportVO"
            },
            "Role": {
                "type": "object",
                "properties": {
                    "createBy": {
                        "type": "string"
                    },
                    "defaultMenuId": {
                        "type": "string"
                    },
                    "defaultTag": {
                        "type": "string"
                    },
                    "flag1": {
                        "type": "string"
                    },
                    "flag2": {
                        "type": "string"
                    },
                    "flag3": {
                        "type": "string"
                    },
                    "flag4": {
                        "type": "string"
                    },
                    "flag5": {
                        "type": "string"
                    },
                    "flag6": {
                        "type": "string"
                    },
                    "isValid": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "menuIds": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "name": {
                        "type": "string"
                    },
                    "note": {
                        "type": "string"
                    },
                    "remark": {
                        "type": "string"
                    },
                    "roleId": {
                        "type": "string"
                    },
                    "systemId": {
                        "type": "string"
                    },
                    "type": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "updateBy": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "Role"
            },
            "ScoreReportVO": {
                "type": "object",
                "properties": {
                    "reportDate": {
                        "type": "string"
                    },
                    "reportId": {
                        "type": "string"
                    },
                    "score": {
                        "type": "number"
                    }
                },
                "title": "ScoreReportVO"
            },
            "SimpleMenuResp": {
                "type": "object",
                "properties": {
                    "checked": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "menuId": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "parentId": {
                        "type": "string"
                    },
                    "shortCutIcon": {
                        "type": "string"
                    },
                    "type": {
                        "type": "integer",
                        "format": "int32"
                    }
                },
                "title": "SimpleMenuResp"
            },
            "StandardConfigVO": {
                "type": "object",
                "properties": {
                    "endPoint": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "levelId": {
                        "type": "string"
                    },
                    "standardLevel": {
                        "type": "string"
                    },
                    "startPoint": {
                        "type": "integer",
                        "format": "int32"
                    }
                },
                "title": "StandardConfigVO"
            },
            "SystemTempPriorityVO": {
                "type": "object",
                "properties": {
                    "defaultMark": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "priorityColor": {
                        "type": "string"
                    },
                    "priorityId": {
                        "type": "string"
                    },
                    "priorityName": {
                        "type": "string"
                    },
                    "tempId": {
                        "type": "string"
                    }
                },
                "title": "SystemTempPriorityVO"
            },
            "SystemTempRoleVO": {
                "type": "object",
                "properties": {
                    "cancelSprint": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "createSprint": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "createTask": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "manage": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "roleLogoType": {
                        "type": "string"
                    },
                    "roleName": {
                        "type": "string"
                    },
                    "tempId": {
                        "type": "string"
                    },
                    "tempRoleId": {
                        "type": "string"
                    },
                    "updateTask": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "updatedSprint": {
                        "type": "integer",
                        "format": "int32"
                    }
                },
                "title": "SystemTempRoleVO"
            },
            "SystemTempStatusVO": {
                "type": "object",
                "properties": {
                    "serial": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "statusColor": {
                        "type": "string"
                    },
                    "statusId": {
                        "type": "string"
                    },
                    "statusName": {
                        "type": "string"
                    },
                    "statusType": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "tempId": {
                        "type": "string"
                    }
                },
                "title": "SystemTempStatusVO"
            },
            "SystemTempTypeVO": {
                "type": "object",
                "properties": {
                    "tempId": {
                        "type": "string"
                    },
                    "typeId": {
                        "type": "string"
                    },
                    "typeLogo": {
                        "type": "string"
                    },
                    "typeName": {
                        "type": "string"
                    }
                },
                "title": "SystemTempTypeVO"
            },
            "SystemTempVO": {
                "type": "object",
                "properties": {
                    "tempId": {
                        "type": "string"
                    },
                    "tempImg": {
                        "type": "string"
                    },
                    "tempName": {
                        "type": "string"
                    },
                    "tempRemark": {
                        "type": "string"
                    }
                },
                "title": "SystemTempVO"
            },
            "User": {
                "type": "object",
                "properties": {
                    "address": {
                        "type": "string"
                    },
                    "alipayId": {
                        "type": "string"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "creatorId": {
                        "type": "string"
                    },
                    "email": {
                        "type": "string"
                    },
                    "isSuperAdmin": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "loginAmount": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "loginAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "mobile": {
                        "type": "string"
                    },
                    "operatorNo": {
                        "type": "string"
                    },
                    "pwd": {
                        "type": "string"
                    },
                    "realName": {
                        "type": "string"
                    },
                    "status": {
                        "type": "string"
                    },
                    "systemId": {
                        "type": "string"
                    },
                    "token": {
                        "type": "string"
                    },
                    "tokenExpire": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "userId": {
                        "type": "string"
                    },
                    "userName": {
                        "type": "string"
                    },
                    "wechatId": {
                        "type": "string"
                    }
                },
                "title": "User"
            },
            "UserScoreReportVO": {
                "type": "object",
                "properties": {
                    "scoreReportList": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/ScoreReportVO"
                        }
                    },
                    "userId": {
                        "type": "string"
                    },
                    "userName": {
                        "type": "string"
                    }
                },
                "title": "UserScoreReportVO"
            },
            "UserTaskVO": {
                "type": "object",
                "properties": {
                    "broTaskId": {
                        "type": "string"
                    },
                    "bugStatusId": {
                        "type": "string"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "creatorId": {
                        "type": "string"
                    },
                    "deadLine": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "description": {
                        "type": "string"
                    },
                    "executorId": {
                        "type": "string"
                    },
                    "finishedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "parTaskId": {
                        "type": "string"
                    },
                    "planId": {
                        "type": "string"
                    },
                    "points": {
                        "type": "number",
                        "format": "double"
                    },
                    "priceFlag": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "priorityId": {
                        "type": "string"
                    },
                    "projectId": {
                        "type": "string"
                    },
                    "projectName": {
                        "type": "string"
                    },
                    "sprintId": {
                        "type": "string"
                    },
                    "startedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "statusId": {
                        "type": "string"
                    },
                    "taskId": {
                        "type": "string"
                    },
                    "title": {
                        "type": "string"
                    },
                    "typeId": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    }
                },
                "title": "UserTaskVO"
            },
            "UserVO": {
                "type": "object",
                "properties": {
                    "birthDate": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "degree": {
                        "type": "string"
                    },
                    "department": {
                        "type": "string"
                    },
                    "educationBackground": {
                        "type": "string"
                    },
                    "employedDate": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "employeeCategory": {
                        "type": "string"
                    },
                    "gender": {
                        "type": "string"
                    },
                    "graduationDate": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "graduationSchool": {
                        "type": "string"
                    },
                    "idNumber": {
                        "type": "string"
                    },
                    "nation": {
                        "type": "string"
                    },
                    "nativePlace": {
                        "type": "string"
                    },
                    "phoneNumber": {
                        "type": "string"
                    },
                    "politicsStatus": {
                        "type": "string"
                    },
                    "position": {
                        "type": "string"
                    },
                    "profession": {
                        "type": "string"
                    },
                    "role": {
                        "type": "string"
                    },
                    "skillsTalents": {
                        "type": "string"
                    },
                    "title": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "userId": {
                        "type": "string"
                    },
                    "userName": {
                        "type": "string"
                    },
                    "workExperience": {
                        "type": "string"
                    },
                    "workingYear": {
                        "type": "string"
                    }
                },
                "title": "UserVO"
            },
            "View": {
                "type": "object",
                "properties": {
                    "contentType": {
                        "type": "string"
                    }
                },
                "title": "View"
            },
            "WorkerVO": {
                "type": "object",
                "properties": {
                    "address": {
                        "type": "string"
                    },
                    "comId": {
                        "type": "string"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "createdBy": {
                        "type": "string"
                    },
                    "fromPlace": {
                        "type": "string"
                    },
                    "gradeId": {
                        "type": "string"
                    },
                    "notion": {
                        "type": "string"
                    },
                    "operatorNo": {
                        "type": "string"
                    },
                    "politicType": {
                        "type": "string"
                    },
                    "postId": {
                        "type": "string"
                    },
                    "rankId": {
                        "type": "string"
                    },
                    "realName": {
                        "type": "string"
                    },
                    "role": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "userIcons": {
                        "type": "string"
                    },
                    "userId": {
                        "type": "string"
                    }
                },
                "title": "WorkerVO"
            }
        }
    }

    a = Excel('interface.xlsx', 'Sheet', 0)
    a.create_excel()
    url_row = 2
    a.write_date(1, 1, 'url')
    a.write_date(1, 2, 'tags')
    a.write_date(1, 3, 'summary')
    a.write_date(1, 4, 'method')
    a.write_date(1, 5, 'parameters')
    a.write_date(1, 6, 'responses')
    for url in data['paths'].keys():
        a.write_date(url_row, 1, url)
        print(data['paths'][url].keys())
        method_row = url_row
        for method in data['paths'][url].keys():
            method_body = data['paths'][url][method]
            a.write_date(method_row, 2, method_body['tags'])
            a.write_date(method_row, 3, method_body['summary'])
            a.write_date(method_row, 4, method)
            try:
                a.write_date(method_row, 5, method_body['parameters'])
            except Exception as e:
                print(e)
            a.write_date(method_row, 6, method_body['responses'])
            method_row = method_row + 1
            print(method)
            print(data['paths'][url][method])
        url_row = url_row + len(data['paths'][url].keys())
