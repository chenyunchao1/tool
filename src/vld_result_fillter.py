# _*_ coding:utf-8 _*_
# 用来过滤vld检测的结果，去掉已知的问题

import sys

excludes = [
    # publib
    "CLuaParser::DoFile()",
    "CLuaParser::CLuaParser()",
    "CLuaParser::CallFunction",
    "luaD_call",
    "CDeathCheck::update()",
    # "CSgsPubFun::UTF8ToGBK()", # 问题已知，已修复
    "CSgsAllocXBlockMg::free",
    "AllocFromSystem", # 暂且排除
    "RedisWorker::RedisWorker()",

    "_Wrap_alloc<std::allocator<char> >::allocate()", # 这个是为啥 std::string(char*) ？？
    "CThread::Start()", 
    "RedisWorkerGroup::Start()", # 单例
    "RedisWorkerGroup::RedisWorkerGroup()", # 单例
    "RedisMgBase::Start()", # 单例
    "CTimerMg::AddTimer()", # 单例


    # logic common
    # "ConnectToCS()", # 问题已知，已修复
 
    # matchserver

    #  tableserver
    "CLookMg::single()", # 单例，写法奇怪，也可以修一下
    "load_generalskininfo_fromxml", # 配置单例，可修复

    # gateserver
    "gateway.cpp (98)", # 单例

    # friendserver
    "imp_load_sys", # 配置单例
    "CExpLevelConfig::imp_load()" , # 配置单例

]


def check_exclude(block_lines):
    all_empty = True
    for idx, line in enumerate(block_lines):
        if any(e in line for e in excludes):
            return True
        if line.strip().startswith("Call Stack") and block_lines[idx+1].strip().startswith("Data"):  # block without stack info
            return True
        all_empty = all_empty and (line.strip() == "")

    if all_empty:
        return True

    return False

def exclude(infile, outfile):
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        block_lines = []
        for line in fin.readlines():
            block_lines.append(line)
            if not line.strip(): # empty line, mean start of a new block
                if not check_exclude(block_lines):
                    fout.writelines(block_lines)
                block_lines = []

        if not check_exclude(block_lines):
            fout.writelines(block_lines)


if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2] if len(sys.argv) == 3 else "out_" + infile
    exclude(infile, outfile)