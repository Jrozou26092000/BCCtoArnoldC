from gen.BCCVisitor import BCCVisitor
from gen.BCCParser import BCCParser


class MyVisitor(BCCVisitor):

    def __init__(self, file):
        self.file = file

    # Visit a parse tree produced by BCCParser#prog.
    def visitProg(self, ctx: BCCParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#f.
    def visitF(self, ctx: BCCParser.FContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#main_prog.
    def visitMain_prog(self, ctx: BCCParser.Main_progContext):
        self.file.write("IT'S SHOWTIME\n")
        self.visitChildren(ctx)
        self.file.write("YOU HAVE BEEN TERMINATED")
        return

    # Visit a parse tree produced by BCCParser#stmt_var_list.
    def visitStmt_var_list(self, ctx: BCCParser.Stmt_var_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#var_dec.
    def visitVar_dec(self, ctx: BCCParser.Var_decContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#stmt_block.
    def visitStmt_block(self, ctx: BCCParser.Stmt_blockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#stmt.
    def visitStmt(self, ctx: BCCParser.StmtContext):
        if ctx.PRINT():
            self.file.write('TALK TO THE HAND '+ctx.getChild(1).getText()+'\n')
        if ctx.INPUT():
            command = 'I WANT TO ASK YOU A BUNCH OF QUESTIONS AND I WANT TO HAVE THEM ANSWERED IMMEDIATELY '
            self.file.write(command+ctx.getChild(1).getText()+'\n')
        if ctx.WHEN():
            command = 'I WANT TO ASK YOU A BUNCH OF QUESTIONS AND I WANT TO HAVE THEM ANSWERED IMMEDIATELY '
            self.file.write(command+ctx.getChild(1).getText()+'\n')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#assignation.
    def visitAssignation(self, ctx: BCCParser.AssignationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#do_block.
    def visitDo_block(self, ctx: BCCParser.Do_blockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#par_lexpr.
    def visitPar_lexpr(self, ctx: BCCParser.Par_lexprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#operation.
    def visitOperation(self, ctx: BCCParser.OperationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#lexpr.
    def visitLexpr(self, ctx: BCCParser.LexprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#nexpr.
    def visitNexpr(self, ctx: BCCParser.NexprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#rexpr.
    def visitRexpr(self, ctx: BCCParser.RexprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#simple_expr.
    def visitSimple_expr(self, ctx: BCCParser.Simple_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#term.
    def visitTerm(self, ctx: BCCParser.TermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#factor.
    def visitFactor(self, ctx: BCCParser.FactorContext):
        return self.visitChildren(ctx)
