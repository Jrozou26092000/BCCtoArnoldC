from gen.BCCVisitor import BCCVisitor
from gen.BCCParser import BCCParser


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
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#assignation.
    def visitAssignation(self, ctx: BCCParser.AssignationContext):
        if ctx.operation():
            self.file.write('GET TO THE CHOPPER ' + ctx.ID().getText()+'\n')
            self.file.write('HERE IS MY INVITATION ')
            self.visitOperation(ctx.operation())
            self.file.write('ENOUGH TALK\n')
        else:
            self.file.write("GET TO THE CHOPPER "+ctx.ID().getText()+'\n')
            self.file.write("HERE IS MY INVITATION "+ctx.ID().getText()+'\n')
            if ctx.getChild(0).getText() == '++':
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

    # Visit a parse tree produced by BCCParser#operation.
    def visitOperation(self, ctx: BCCParser.OperationContext):
        if ctx.getChild(0).getText() == '++':
            self.file.write(ctx.parentCtx.ID().getText()+'\n')
            self.file.write("GET UP 1\n")
            return
        if ctx.getChild(0).getText() == '--':
            self.file.write(ctx.parentCtx.ID().getText()+'\n')
            self.file.write("GET DOWN 1\n")
            return
        var = self.visitLexpr(ctx.lexpr())
        if ctx.getChild(0).getText() == ':=':
            self.file.write(var + '\n')
        if ctx.getChild(0).getText() == '+=':
            self.file.write('GET UP' + var + '\n')
        if ctx.getChild(0).getText() == '-=':
            self.file.write('GET DOWN' + var + '\n')
        if ctx.getChild(0).getText() == '*=':
            self.file.write("YOU'RE FIRED" + var + '\n')
        if ctx.getChild(0).getText() == '/=':
            self.file.write('HE HAD TO SPLIT' + var + '\n')
        if ctx.getChild(0).getText() == '%=':
            self.file.write('I LET HIM GO' + var + '\n')
        return

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
        # for argunment in children:
            # if argunmment
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#term.
    def visitTerm(self, ctx: BCCParser.TermContext):
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
