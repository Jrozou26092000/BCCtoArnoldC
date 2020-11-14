from gen.BCCVisitor import BCCVisitor
from gen.BCCParser import BCCParser
import re


class MyVisitor(BCCVisitor):

    def __init__(self, file):
        self.file = file
        self.result = 0

    # Visit a parse tree produced by BCCParser#prog.
    def visitProg(self, ctx: BCCParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#f.
    def visitF(self, ctx: BCCParser.FContext):
        self.file.write('LISTEN TO ME VERY CAREFULLY '+ctx.FID().getText()[1:]+'\n')
        for dec in ctx.var_dec():
            self.file.write('I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE '+dec.ID().getText()+'\n')
        self.visitChildren(ctx)
        self.file.write('HASTA LA VISTA, BABY\n')

    # Visit a parse tree produced by BCCParser#main_prog.
    def visitMain_prog(self, ctx: BCCParser.Main_progContext):
        self.file.write("IT'S SHOWTIME\n")
        self.visitChildren(ctx)
        self.file.write("YOU HAVE BEEN TERMINATED")
        return

    # Visit a parse tree produced by BCCParser#stmt_var_list.
    def visitStmt_var_list(self, ctx: BCCParser.Stmt_var_listContext):
        for var in ctx.var_dec():
            self.file.write('HEY CHRISTMAS TREE '+var.ID().getText()+'\n')
            self.file.write('YOU SET US UP 0\n')

    # Visit a parse tree produced by BCCParser#var_dec.
    def visitVar_dec(self, ctx: BCCParser.Var_decContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#stmt_block.
    def visitStmt_block(self, ctx: BCCParser.Stmt_blockContext):
        if 'return' in ctx.getText():
            self.file.write("GIVE THESE PEOPLE AIR")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#stmt.
    def visitStmt(self, ctx: BCCParser.StmtContext):
        if ctx.PRINT():
            children = self.visitLexpr(ctx.lexpr()[0])
            self.file.write('TALK TO THE HAND '+str(children))
            self.file.write('\n')
            return
        if ctx.INPUT():
            command = 'I WANT TO ASK YOU A BUNCH OF QUESTIONS AND I WANT TO HAVE THEM ANSWERED IMMEDIATELY '
            self.file.write(command+ctx.getChild(1).getText()+'\n')
            return
        if ctx.WHEN():
            condition = self.visitPar_lexpr(ctx.par_lexpr())
            self.file.write("BECAUSE I'M GOING TO SAY PLEASE "+condition+'\n')
            self.visitChildren(ctx)
            self.file.write("YOU HAVE NO RESPECT FOR LOGIC\n")
            return
        if ctx.RETURN():
            self.file.write("I'LL BE BACK "+ctx.getChild(1).getText()+'\n')
            return
        if ctx.IF():
            condition = self.visitPar_lexpr(ctx.par_lexpr())
            self.file.write("BECAUSE I'M GOING TO SAY PLEASE "+condition+'\n')
            self.visitDo_block(ctx.do_block()[0])
            self.file.write("BULLSHIT \n")
            self.visitStmt_block(ctx.stmt_block())
            self.file.write("YOU HAVE NO RESPECT FOR LOGIC\n")
            return
        if ctx.CICLE():
            if ctx.CICLE().getText() == 'unless':
                condition = self.visitPar_lexpr(ctx.par_lexpr())
                self.file.write('HEY CHRISTMAS TREE result'+str(self.result)+'\n')
                self.file.write('YOU SET US UP 0\n')
                self.file.write("GET TO THE CHOPPER result"+str(self.result)+'\n')
                self.file.write("HERE IS MY INVITATION "+str(condition)+'\n')
                self.file.write("GET UP 1\n")
                self.file.write("I LET HIM GO 2")
                self.file.write("ENOUGH TALK\n")
                self.file.write("BECAUSE I'M GOING TO SAY PLEASE result"+str(self.result)+'\n')
                self.visitChildren(ctx)
                self.file.write("YOU HAVE NO RESPECT FOR LOGIC\n")
                return
            if ctx.CICLE().getText() == 'while':
                value = self.visitPar_lexpr(ctx.par_lexpr())
                self.file.write("STICK AROUND "+value)
                self.visitChildren(ctx)

                self.file.write("CHILL")
                return
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#assignation.
    def visitAssignation(self, ctx: BCCParser.AssignationContext):
        if ctx.OPERATION():
            var = self.visitLexpr(ctx.lexpr())
            self.file.write('GET TO THE CHOPPER ' + ctx.ID().getText()+'\n')
            self.file.write('HERE IS MY INVITATION ')
            if ctx.OPERATION().getText() == ':=':
                self.file.write(var + '\n')
            if ctx.OPERATION().getText() == '+=':
                self.file.write('GET UP' + var + '\n')
            if ctx.OPERATION().getText() == '-=':
                self.file.write('GET DOWN' + var + '\n')
            if ctx.OPERATION().getText() == '*=':
                self.file.write("YOU'RE FIRED" + var + '\n')
            if ctx.OPERATION().getText() == '/=':
                self.file.write('HE HAD TO SPLIT' + var + '\n')
            if ctx.OPERATION().getText() == '%=':
                self.file.write('I LET HIM GO' + var + '\n')
            self.file.write('ENOUGH TALK\n')
        else:
            self.file.write("GET TO THE CHOPPER "+ctx.ID().getText()+'\n')
            self.file.write("HERE IS MY INVITATION "+ctx.ID().getText()+'\n')
            if ctx.getChild(0).getText() == '++' or ctx.getChild(1).getText() == '++':
                self.file.write("GET UP 1\n")
            else:
                self.file.write("GET DOWN 1\n")
            self.file.write("ENOUGH TALK\n")

    # Visit a parse tree produced by BCCParser#do_block.
    def visitDo_block(self, ctx: BCCParser.Do_blockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#par_lexpr.
    def visitPar_lexpr(self, ctx: BCCParser.Par_lexprContext):
        return self.visitLexpr(ctx.lexpr())

        # Visit a parse tree produced by BCCParser#lexpr.
    def visitLexpr(self, ctx: BCCParser.LexprContext):
        # if ctx.getChildCount() > 1:
        #     self.visitNexpr(ctx.getChild(0))
        #     if ctx.getChild(1) == ctx.AND():
        #         self.file.write('KNOCK KNOCK')
        #     if ctx.getChild(1) == ctx.OR():
        #         self.file.write('CONSIDER THAT A DIVORCE')
        #     self.visitNexpr(ctx.getChild(2))
        # else:
        #     self.visitNexpr(ctx.getChild(0))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#nexpr.
    def visitNexpr(self, ctx: BCCParser.NexprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#rexpr.
    def visitRexpr(self, ctx: BCCParser.RexprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#simple_expr.
    def visitSimple_expr(self, ctx: BCCParser.Simple_exprContext):
        # Revisar aquí lo de el pos - in/de - cremento cuando se retorn uno solo --> c: a++.

        # print(ctx.getChild(0).getText())
        # if ctx.getChild(1) and ctx.getChild(1).getText() == '*':
        #     print("OK")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#term.
    def visitTerm(self, ctx: BCCParser.TermContext):
        factor = list()
        for argumment in ctx.factor():
            factor.append(self.visitFactor(argumment))
        # Revisar --> Se está imprimiendo el último no terminal dos veces.
        if len(factor)>1:
            i = 1
            for symbol in factor:
                print(symbol)
                if len(str(symbol)) > 1 and (str(symbol)[1] == '+' or str(symbol)[1] == '-'):
                    print("OK")
                    # self.file.write("GET TO THE CHOPPER "+(str(symbol)[1]+'\n')
                    # self.file.write("HERE IS MY INVITATION "+(str(symbol)[1]+'\n')
                    # if '++' in str(symbol):
                    #     self.file.write("GET UP 1\n")
                    # else:
                    #     self.file.write("GET DOWN 1\n")
                    # self.file.write("ENOUGH TALK\n")
                    # return symbol
                elif '++' in str(symbol) or '--' in str(symbol):
                    self.file.write(str(symbol)[0]+'\n')
                else:
                    self.file.write(str(symbol)+'\n')
                if ctx.getChild(i):
                    if ctx.getChild(i).getText() == '*':
                        self.file.write("YOU'RE FIRED ")
                    elif ctx.getChild(i).getText() == '/':
                        self.file.write("HE HAD TO SPLIT ")
                    elif ctx.getChild(i).getText() == '%':
                        self.file.write("I LET HIM GO ")
                i += 2
        else:
            return factor[0]
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#factor.
    def visitFactor(self, ctx: BCCParser.FactorContext):
        if ctx.TK_BOOL():
            if ctx.getText() == 'true':
                return "@NO PROBLEMO"
            else:
                return "@I LIED"
        if ctx.TK_NUM():
            return ctx.getText()
        if ctx.ID():
            if ctx.getChildCount() > 1:
                if ctx.getChild(1) == ctx.ID():
                    self.file.write("GET TO THE CHOPPER "+ctx.ID().getText()+'\n')
                    self.file.write("HERE IS MY INVITATION "+ctx.ID().getText()+'\n')
                    if '++' in ctx.getText():
                        self.file.write("GET UP 1\n")
                    else:
                        self.file.write("GET DOWN 1\n")
                    self.file.write("ENOUGH TALK\n")
                    return ctx.ID().getText()
            return ctx.getText()
        if ctx.FID():
            children = list()
            for i in ctx.lexpr():
                children.append(self.visitLexpr(i))
            self.file.write('HEY CHRISTMAS TREE result'+str(self.result)+'\n')
            self.file.write('YOU SET US UP 0\n')
            self.file.write("GET YOUR ASS TO MARS result"+str(self.result)+'\n')
            self.file.write("DO IT NOW "+ctx.FID().getText()[1:])
            if children:
                for argument in children:
                    if '--' in argument or '++' in argument:
                        self.file.write(" "+argument[:-2])
                    else:
                        self.file.write(" "+argument)
            self.file.write("\n")
            if children:
                for argument in children:
                    if '--' in argument or '++' in argument:
                        self.file.write("GET TO THE CHOPPER "+argument[:-2]+'\n')
                        self.file.write("HERE IS MY INVITATION "+argument[:-2]+'\n')
                        if '++' in argument:
                            self.file.write("GET UP 1\n")
                        else:
                            self.file.write("GET DOWN 1\n")
                        self.file.write("ENOUGH TALK\n")
            self.result = self.result+1
            return "result"+str(self.result-1)
        return self.visitChildren(ctx)
