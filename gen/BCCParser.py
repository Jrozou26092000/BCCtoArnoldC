# Generated from /home/crisvo/IdeaProjects/BCCtoArnoldC/grammar/BCC.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\62")
        buf.write("\u00e9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\7\2$\n\2\f\2\16")
        buf.write("\2\'\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3")
        buf.write("\63\n\3\f\3\16\3\66\13\3\5\38\n\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\7\4@\n\4\f\4\16\4C\13\4\3\4\3\4\3\5\3\5\3\5\3\5\7")
        buf.write("\5K\n\5\f\5\16\5N\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\7\7X\n\7\f\7\16\7[\13\7\3\7\3\7\5\7_\n\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0093\n\b\3\t\3\t\3\t\3")
        buf.write("\t\5\t\u0099\n\t\3\t\3\t\3\t\3\t\5\t\u009f\n\t\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\7\f\u00ad")
        buf.write("\n\f\f\f\16\f\u00b0\13\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b8")
        buf.write("\n\r\3\16\3\16\3\16\5\16\u00bd\n\16\3\17\3\17\3\17\7\17")
        buf.write("\u00c2\n\17\f\17\16\17\u00c5\13\17\3\20\3\20\3\20\7\20")
        buf.write("\u00ca\n\20\f\20\16\20\u00cd\13\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u00df\n\21\f\21\16\21\u00e2\13\21\5\21\u00e4")
        buf.write("\n\21\3\21\5\21\u00e7\n\21\3\21\2\2\22\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \2\6\3\2\r\16\3\2\20\25\3\2\26")
        buf.write("\27\3\2\30\32\2\u00fb\2%\3\2\2\2\4*\3\2\2\2\6=\3\2\2\2")
        buf.write("\bF\3\2\2\2\nQ\3\2\2\2\f^\3\2\2\2\16\u0092\3\2\2\2\20")
        buf.write("\u009e\3\2\2\2\22\u00a0\3\2\2\2\24\u00a3\3\2\2\2\26\u00a7")
        buf.write("\3\2\2\2\30\u00b7\3\2\2\2\32\u00b9\3\2\2\2\34\u00be\3")
        buf.write("\2\2\2\36\u00c6\3\2\2\2 \u00e6\3\2\2\2\"$\5\4\3\2#\"\3")
        buf.write("\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2")
        buf.write("\2\2()\5\6\4\2)\3\3\2\2\2*+\7\3\2\2+,\7\35\2\2,-\7\4\2")
        buf.write("\2-.\7\61\2\2.\67\7\5\2\2/\64\5\n\6\2\60\61\7\6\2\2\61")
        buf.write("\63\5\n\6\2\62\60\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2")
        buf.write("\64\65\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\67/\3\2\2\2\67")
        buf.write("8\3\2\2\289\3\2\2\29:\7\7\2\2:;\5\b\5\2;<\5\f\7\2<\5\3")
        buf.write("\2\2\2=A\5\b\5\2>@\5\16\b\2?>\3\2\2\2@C\3\2\2\2A?\3\2")
        buf.write("\2\2AB\3\2\2\2BD\3\2\2\2CA\3\2\2\2DE\7\b\2\2E\7\3\2\2")
        buf.write("\2FG\7\t\2\2GL\5\n\6\2HI\7\6\2\2IK\5\n\6\2JH\3\2\2\2K")
        buf.write("N\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MO\3\2\2\2NL\3\2\2\2OP\7")
        buf.write("\n\2\2P\t\3\2\2\2QR\7\62\2\2RS\7\4\2\2ST\7\61\2\2T\13")
        buf.write("\3\2\2\2UY\7\13\2\2VX\5\16\b\2WV\3\2\2\2X[\3\2\2\2YW\3")
        buf.write("\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\_\7\f\2\2]_\5\16")
        buf.write("\b\2^U\3\2\2\2^]\3\2\2\2_\r\3\2\2\2`a\7 \2\2ab\5\26\f")
        buf.write("\2bc\7\n\2\2c\u0093\3\2\2\2de\7!\2\2ef\7\62\2\2f\u0093")
        buf.write("\7\n\2\2gh\7\"\2\2hi\5\24\13\2ij\5\22\n\2j\u0093\3\2\2")
        buf.write("\2kl\7#\2\2lm\5\24\13\2mn\5\22\n\2no\7$\2\2op\5\f\7\2")
        buf.write("p\u0093\3\2\2\2qr\7%\2\2rs\5\24\13\2st\5\22\n\2t\u0093")
        buf.write("\3\2\2\2uv\5\22\n\2vw\7&\2\2wx\5\24\13\2x\u0093\3\2\2")
        buf.write("\2yz\7\'\2\2z{\5\26\f\2{|\7\n\2\2|\u0093\3\2\2\2}~\7(")
        buf.write("\2\2~\u0093\5\f\7\2\177\u0080\7)\2\2\u0080\u0081\7\36")
        buf.write("\2\2\u0081\u0082\7\4\2\2\u0082\u0093\5\f\7\2\u0083\u0084")
        buf.write("\7*\2\2\u0084\u0085\7\5\2\2\u0085\u0086\5\26\f\2\u0086")
        buf.write("\u0087\7\n\2\2\u0087\u0088\5\26\f\2\u0088\u0089\7\n\2")
        buf.write("\2\u0089\u008a\5\20\t\2\u008a\u008b\7\7\2\2\u008b\u008c")
        buf.write("\5\22\n\2\u008c\u0093\3\2\2\2\u008d\u008e\7+\2\2\u008e")
        buf.write("\u0093\7\n\2\2\u008f\u0090\7,\2\2\u0090\u0093\7\n\2\2")
        buf.write("\u0091\u0093\5\20\t\2\u0092`\3\2\2\2\u0092d\3\2\2\2\u0092")
        buf.write("g\3\2\2\2\u0092k\3\2\2\2\u0092q\3\2\2\2\u0092u\3\2\2\2")
        buf.write("\u0092y\3\2\2\2\u0092}\3\2\2\2\u0092\177\3\2\2\2\u0092")
        buf.write("\u0083\3\2\2\2\u0092\u008d\3\2\2\2\u0092\u008f\3\2\2\2")
        buf.write("\u0092\u0091\3\2\2\2\u0093\17\3\2\2\2\u0094\u0098\7\62")
        buf.write("\2\2\u0095\u0096\7\37\2\2\u0096\u0099\5\26\f\2\u0097\u0099")
        buf.write("\t\2\2\2\u0098\u0095\3\2\2\2\u0098\u0097\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\u009f\7\n\2\2\u009b\u009c\t\2\2\2")
        buf.write("\u009c\u009d\7\62\2\2\u009d\u009f\7\n\2\2\u009e\u0094")
        buf.write("\3\2\2\2\u009e\u009b\3\2\2\2\u009f\21\3\2\2\2\u00a0\u00a1")
        buf.write("\7\17\2\2\u00a1\u00a2\5\f\7\2\u00a2\23\3\2\2\2\u00a3\u00a4")
        buf.write("\7\5\2\2\u00a4\u00a5\5\26\f\2\u00a5\u00a6\7\7\2\2\u00a6")
        buf.write("\25\3\2\2\2\u00a7\u00ae\5\30\r\2\u00a8\u00a9\7-\2\2\u00a9")
        buf.write("\u00ad\5\30\r\2\u00aa\u00ab\7.\2\2\u00ab\u00ad\5\30\r")
        buf.write("\2\u00ac\u00a8\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00b0")
        buf.write("\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\27\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b2\7/\2\2\u00b2")
        buf.write("\u00b3\7\5\2\2\u00b3\u00b4\5\26\f\2\u00b4\u00b5\7\7\2")
        buf.write("\2\u00b5\u00b8\3\2\2\2\u00b6\u00b8\5\32\16\2\u00b7\u00b1")
        buf.write("\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\31\3\2\2\2\u00b9\u00bc")
        buf.write("\5\34\17\2\u00ba\u00bb\t\3\2\2\u00bb\u00bd\5\34\17\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\33\3\2\2\2\u00be")
        buf.write("\u00c3\5\36\20\2\u00bf\u00c0\t\4\2\2\u00c0\u00c2\5\36")
        buf.write("\20\2\u00c1\u00bf\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\35\3\2\2\2\u00c5\u00c3")
        buf.write("\3\2\2\2\u00c6\u00cb\5 \21\2\u00c7\u00c8\t\5\2\2\u00c8")
        buf.write("\u00ca\5 \21\2\u00c9\u00c7\3\2\2\2\u00ca\u00cd\3\2\2\2")
        buf.write("\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\37\3\2")
        buf.write("\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00e7\7\36\2\2\u00cf\u00e7")
        buf.write("\7\60\2\2\u00d0\u00d1\7\62\2\2\u00d1\u00e7\t\2\2\2\u00d2")
        buf.write("\u00d3\t\2\2\2\u00d3\u00e7\7\62\2\2\u00d4\u00e7\7\62\2")
        buf.write("\2\u00d5\u00d6\7\5\2\2\u00d6\u00d7\5\26\f\2\u00d7\u00d8")
        buf.write("\7\7\2\2\u00d8\u00e7\3\2\2\2\u00d9\u00da\7\35\2\2\u00da")
        buf.write("\u00e3\7\5\2\2\u00db\u00e0\5\26\f\2\u00dc\u00dd\7\6\2")
        buf.write("\2\u00dd\u00df\5\26\f\2\u00de\u00dc\3\2\2\2\u00df\u00e2")
        buf.write("\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1")
        buf.write("\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00db\3\2\2\2")
        buf.write("\u00e3\u00e4\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e7\7")
        buf.write("\7\2\2\u00e6\u00ce\3\2\2\2\u00e6\u00cf\3\2\2\2\u00e6\u00d0")
        buf.write("\3\2\2\2\u00e6\u00d2\3\2\2\2\u00e6\u00d4\3\2\2\2\u00e6")
        buf.write("\u00d5\3\2\2\2\u00e6\u00d9\3\2\2\2\u00e7!\3\2\2\2\25%")
        buf.write("\64\67ALY^\u0092\u0098\u009e\u00ac\u00ae\u00b7\u00bc\u00c3")
        buf.write("\u00cb\u00e0\u00e3\u00e6")
        return buf.getvalue()


class BCCParser ( Parser ):

    grammarFileName = "BCC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "':'", "'('", "','", "')'", 
                     "'end'", "'var'", "';'", "'{'", "'}'", "'++'", "'--'", 
                     "'do'", "'<'", "'=='", "'<='", "'>'", "'>='", "'!='", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'print'", "'input'", 
                     "'when'", "'if'", "'else'", "<INVALID>", "<INVALID>", 
                     "'return'", "'loop'", "'repeat'", "'for'", "'next'", 
                     "'break'", "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "COMMENT", "FID", "TK_NUM", "OPERATION", 
                      "PRINT", "INPUT", "WHEN", "IF", "ELSE", "CICLE", "CICLE2", 
                      "RETURN", "LOOP", "REPEAT", "FOR", "NEXT", "BREAK", 
                      "AND", "OR", "NOT", "TK_BOOL", "DATATYPE", "ID" ]

    RULE_prog = 0
    RULE_f = 1
    RULE_main_prog = 2
    RULE_stmt_var_list = 3
    RULE_var_dec = 4
    RULE_stmt_block = 5
    RULE_stmt = 6
    RULE_assignation = 7
    RULE_do_block = 8
    RULE_par_lexpr = 9
    RULE_lexpr = 10
    RULE_nexpr = 11
    RULE_rexpr = 12
    RULE_simple_expr = 13
    RULE_term = 14
    RULE_factor = 15

    ruleNames =  [ "prog", "f", "main_prog", "stmt_var_list", "var_dec", 
                   "stmt_block", "stmt", "assignation", "do_block", "par_lexpr", 
                   "lexpr", "nexpr", "rexpr", "simple_expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    WS=25
    COMMENT=26
    FID=27
    TK_NUM=28
    OPERATION=29
    PRINT=30
    INPUT=31
    WHEN=32
    IF=33
    ELSE=34
    CICLE=35
    CICLE2=36
    RETURN=37
    LOOP=38
    REPEAT=39
    FOR=40
    NEXT=41
    BREAK=42
    AND=43
    OR=44
    NOT=45
    TK_BOOL=46
    DATATYPE=47
    ID=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_prog(self):
            return self.getTypedRuleContext(BCCParser.Main_progContext,0)


        def f(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.FContext)
            else:
                return self.getTypedRuleContext(BCCParser.FContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = BCCParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__0:
                self.state = 32
                self.f()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.main_prog()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FID(self):
            return self.getToken(BCCParser.FID, 0)

        def DATATYPE(self):
            return self.getToken(BCCParser.DATATYPE, 0)

        def stmt_var_list(self):
            return self.getTypedRuleContext(BCCParser.Stmt_var_listContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(BCCParser.Stmt_blockContext,0)


        def var_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.Var_decContext)
            else:
                return self.getTypedRuleContext(BCCParser.Var_decContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_f

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF" ):
                return visitor.visitF(self)
            else:
                return visitor.visitChildren(self)




    def f(self):

        localctx = BCCParser.FContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_f)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(BCCParser.T__0)
            self.state = 41
            self.match(BCCParser.FID)
            self.state = 42
            self.match(BCCParser.T__1)
            self.state = 43
            self.match(BCCParser.DATATYPE)
            self.state = 44
            self.match(BCCParser.T__2)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BCCParser.ID:
                self.state = 45
                self.var_dec()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BCCParser.T__3:
                    self.state = 46
                    self.match(BCCParser.T__3)
                    self.state = 47
                    self.var_dec()
                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 55
            self.match(BCCParser.T__4)
            self.state = 56
            self.stmt_var_list()
            self.state = 57
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_progContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_list(self):
            return self.getTypedRuleContext(BCCParser.Stmt_var_listContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.StmtContext)
            else:
                return self.getTypedRuleContext(BCCParser.StmtContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_main_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_prog" ):
                return visitor.visitMain_prog(self)
            else:
                return visitor.visitChildren(self)




    def main_prog(self):

        localctx = BCCParser.Main_progContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.stmt_var_list()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__10) | (1 << BCCParser.T__11) | (1 << BCCParser.T__12) | (1 << BCCParser.PRINT) | (1 << BCCParser.INPUT) | (1 << BCCParser.WHEN) | (1 << BCCParser.IF) | (1 << BCCParser.CICLE) | (1 << BCCParser.RETURN) | (1 << BCCParser.LOOP) | (1 << BCCParser.REPEAT) | (1 << BCCParser.FOR) | (1 << BCCParser.NEXT) | (1 << BCCParser.BREAK) | (1 << BCCParser.ID))) != 0):
                self.state = 60
                self.stmt()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(BCCParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.Var_decContext)
            else:
                return self.getTypedRuleContext(BCCParser.Var_decContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_stmt_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_list" ):
                return visitor.visitStmt_var_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_var_list(self):

        localctx = BCCParser.Stmt_var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(BCCParser.T__6)
            self.state = 69
            self.var_dec()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__3:
                self.state = 70
                self.match(BCCParser.T__3)
                self.state = 71
                self.var_dec()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.match(BCCParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BCCParser.ID, 0)

        def DATATYPE(self):
            return self.getToken(BCCParser.DATATYPE, 0)

        def getRuleIndex(self):
            return BCCParser.RULE_var_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dec" ):
                return visitor.visitVar_dec(self)
            else:
                return visitor.visitChildren(self)




    def var_dec(self):

        localctx = BCCParser.Var_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(BCCParser.ID)
            self.state = 80
            self.match(BCCParser.T__1)
            self.state = 81
            self.match(BCCParser.DATATYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.StmtContext)
            else:
                return self.getTypedRuleContext(BCCParser.StmtContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_stmt_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = BCCParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt_block)
        self._la = 0 # Token type
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(BCCParser.T__8)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__10) | (1 << BCCParser.T__11) | (1 << BCCParser.T__12) | (1 << BCCParser.PRINT) | (1 << BCCParser.INPUT) | (1 << BCCParser.WHEN) | (1 << BCCParser.IF) | (1 << BCCParser.CICLE) | (1 << BCCParser.RETURN) | (1 << BCCParser.LOOP) | (1 << BCCParser.REPEAT) | (1 << BCCParser.FOR) | (1 << BCCParser.NEXT) | (1 << BCCParser.BREAK) | (1 << BCCParser.ID))) != 0):
                    self.state = 84
                    self.stmt()
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 90
                self.match(BCCParser.T__9)
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11, BCCParser.T__12, BCCParser.PRINT, BCCParser.INPUT, BCCParser.WHEN, BCCParser.IF, BCCParser.CICLE, BCCParser.RETURN, BCCParser.LOOP, BCCParser.REPEAT, BCCParser.FOR, BCCParser.NEXT, BCCParser.BREAK, BCCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(BCCParser.PRINT, 0)

        def lexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.LexprContext)
            else:
                return self.getTypedRuleContext(BCCParser.LexprContext,i)


        def INPUT(self):
            return self.getToken(BCCParser.INPUT, 0)

        def ID(self):
            return self.getToken(BCCParser.ID, 0)

        def WHEN(self):
            return self.getToken(BCCParser.WHEN, 0)

        def par_lexpr(self):
            return self.getTypedRuleContext(BCCParser.Par_lexprContext,0)


        def do_block(self):
            return self.getTypedRuleContext(BCCParser.Do_blockContext,0)


        def IF(self):
            return self.getToken(BCCParser.IF, 0)

        def ELSE(self):
            return self.getToken(BCCParser.ELSE, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(BCCParser.Stmt_blockContext,0)


        def CICLE(self):
            return self.getToken(BCCParser.CICLE, 0)

        def CICLE2(self):
            return self.getToken(BCCParser.CICLE2, 0)

        def RETURN(self):
            return self.getToken(BCCParser.RETURN, 0)

        def LOOP(self):
            return self.getToken(BCCParser.LOOP, 0)

        def REPEAT(self):
            return self.getToken(BCCParser.REPEAT, 0)

        def TK_NUM(self):
            return self.getToken(BCCParser.TK_NUM, 0)

        def FOR(self):
            return self.getToken(BCCParser.FOR, 0)

        def assignation(self):
            return self.getTypedRuleContext(BCCParser.AssignationContext,0)


        def NEXT(self):
            return self.getToken(BCCParser.NEXT, 0)

        def BREAK(self):
            return self.getToken(BCCParser.BREAK, 0)

        def getRuleIndex(self):
            return BCCParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BCCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stmt)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.PRINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(BCCParser.PRINT)
                self.state = 95
                self.lexpr()
                self.state = 96
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.INPUT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(BCCParser.INPUT)
                self.state = 99
                self.match(BCCParser.ID)
                self.state = 100
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.WHEN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.match(BCCParser.WHEN)
                self.state = 102
                self.par_lexpr()
                self.state = 103
                self.do_block()
                pass
            elif token in [BCCParser.IF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.match(BCCParser.IF)
                self.state = 106
                self.par_lexpr()
                self.state = 107
                self.do_block()
                self.state = 108
                self.match(BCCParser.ELSE)
                self.state = 109
                self.stmt_block()
                pass
            elif token in [BCCParser.CICLE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 111
                self.match(BCCParser.CICLE)
                self.state = 112
                self.par_lexpr()
                self.state = 113
                self.do_block()
                pass
            elif token in [BCCParser.T__12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 115
                self.do_block()
                self.state = 116
                self.match(BCCParser.CICLE2)
                self.state = 117
                self.par_lexpr()
                pass
            elif token in [BCCParser.RETURN]:
                self.enterOuterAlt(localctx, 7)
                self.state = 119
                self.match(BCCParser.RETURN)
                self.state = 120
                self.lexpr()
                self.state = 121
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.LOOP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 123
                self.match(BCCParser.LOOP)
                self.state = 124
                self.stmt_block()
                pass
            elif token in [BCCParser.REPEAT]:
                self.enterOuterAlt(localctx, 9)
                self.state = 125
                self.match(BCCParser.REPEAT)
                self.state = 126
                self.match(BCCParser.TK_NUM)
                self.state = 127
                self.match(BCCParser.T__1)
                self.state = 128
                self.stmt_block()
                pass
            elif token in [BCCParser.FOR]:
                self.enterOuterAlt(localctx, 10)
                self.state = 129
                self.match(BCCParser.FOR)
                self.state = 130
                self.match(BCCParser.T__2)
                self.state = 131
                self.lexpr()
                self.state = 132
                self.match(BCCParser.T__7)
                self.state = 133
                self.lexpr()
                self.state = 134
                self.match(BCCParser.T__7)
                self.state = 135
                self.assignation()
                self.state = 136
                self.match(BCCParser.T__4)
                self.state = 137
                self.do_block()
                pass
            elif token in [BCCParser.NEXT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 139
                self.match(BCCParser.NEXT)
                self.state = 140
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.BREAK]:
                self.enterOuterAlt(localctx, 12)
                self.state = 141
                self.match(BCCParser.BREAK)
                self.state = 142
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11, BCCParser.ID]:
                self.enterOuterAlt(localctx, 13)
                self.state = 143
                self.assignation()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BCCParser.ID, 0)

        def OPERATION(self):
            return self.getToken(BCCParser.OPERATION, 0)

        def lexpr(self):
            return self.getTypedRuleContext(BCCParser.LexprContext,0)


        def getRuleIndex(self):
            return BCCParser.RULE_assignation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignation" ):
                return visitor.visitAssignation(self)
            else:
                return visitor.visitChildren(self)




    def assignation(self):

        localctx = BCCParser.AssignationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignation)
        self._la = 0 # Token type
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(BCCParser.ID)
                self.state = 150
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BCCParser.OPERATION]:
                    self.state = 147
                    self.match(BCCParser.OPERATION)
                    self.state = 148
                    self.lexpr()
                    pass
                elif token in [BCCParser.T__10, BCCParser.T__11]:
                    self.state = 149
                    _la = self._input.LA(1)
                    if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 152
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 154
                self.match(BCCParser.ID)
                self.state = 155
                self.match(BCCParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_block(self):
            return self.getTypedRuleContext(BCCParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return BCCParser.RULE_do_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_block" ):
                return visitor.visitDo_block(self)
            else:
                return visitor.visitChildren(self)




    def do_block(self):

        localctx = BCCParser.Do_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_do_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(BCCParser.T__12)
            self.state = 159
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Par_lexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexpr(self):
            return self.getTypedRuleContext(BCCParser.LexprContext,0)


        def getRuleIndex(self):
            return BCCParser.RULE_par_lexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar_lexpr" ):
                return visitor.visitPar_lexpr(self)
            else:
                return visitor.visitChildren(self)




    def par_lexpr(self):

        localctx = BCCParser.Par_lexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_par_lexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(BCCParser.T__2)
            self.state = 162
            self.lexpr()
            self.state = 163
            self.match(BCCParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.NexprContext)
            else:
                return self.getTypedRuleContext(BCCParser.NexprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(BCCParser.AND)
            else:
                return self.getToken(BCCParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(BCCParser.OR)
            else:
                return self.getToken(BCCParser.OR, i)

        def getRuleIndex(self):
            return BCCParser.RULE_lexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexpr" ):
                return visitor.visitLexpr(self)
            else:
                return visitor.visitChildren(self)




    def lexpr(self):

        localctx = BCCParser.LexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_lexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.nexpr()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.AND or _la==BCCParser.OR:
                self.state = 170
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BCCParser.AND]:
                    self.state = 166
                    self.match(BCCParser.AND)
                    self.state = 167
                    self.nexpr()
                    pass
                elif token in [BCCParser.OR]:
                    self.state = 168
                    self.match(BCCParser.OR)
                    self.state = 169
                    self.nexpr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BCCParser.NOT, 0)

        def lexpr(self):
            return self.getTypedRuleContext(BCCParser.LexprContext,0)


        def rexpr(self):
            return self.getTypedRuleContext(BCCParser.RexprContext,0)


        def getRuleIndex(self):
            return BCCParser.RULE_nexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNexpr" ):
                return visitor.visitNexpr(self)
            else:
                return visitor.visitChildren(self)




    def nexpr(self):

        localctx = BCCParser.NexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_nexpr)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(BCCParser.NOT)
                self.state = 176
                self.match(BCCParser.T__2)
                self.state = 177
                self.lexpr()
                self.state = 178
                self.match(BCCParser.T__4)
                pass
            elif token in [BCCParser.T__2, BCCParser.T__10, BCCParser.T__11, BCCParser.FID, BCCParser.TK_NUM, BCCParser.TK_BOOL, BCCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.rexpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.Simple_exprContext)
            else:
                return self.getTypedRuleContext(BCCParser.Simple_exprContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_rexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRexpr" ):
                return visitor.visitRexpr(self)
            else:
                return visitor.visitChildren(self)




    def rexpr(self):

        localctx = BCCParser.RexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_rexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.simple_expr()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__13) | (1 << BCCParser.T__14) | (1 << BCCParser.T__15) | (1 << BCCParser.T__16) | (1 << BCCParser.T__17) | (1 << BCCParser.T__18))) != 0):
                self.state = 184
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__13) | (1 << BCCParser.T__14) | (1 << BCCParser.T__15) | (1 << BCCParser.T__16) | (1 << BCCParser.T__17) | (1 << BCCParser.T__18))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 185
                self.simple_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.TermContext)
            else:
                return self.getTypedRuleContext(BCCParser.TermContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_simple_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_expr" ):
                return visitor.visitSimple_expr(self)
            else:
                return visitor.visitChildren(self)




    def simple_expr(self):

        localctx = BCCParser.Simple_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_simple_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.term()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__19 or _la==BCCParser.T__20:
                self.state = 189
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__19 or _la==BCCParser.T__20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 190
                self.term()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.FactorContext)
            else:
                return self.getTypedRuleContext(BCCParser.FactorContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = BCCParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.factor()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__21) | (1 << BCCParser.T__22) | (1 << BCCParser.T__23))) != 0):
                self.state = 197
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__21) | (1 << BCCParser.T__22) | (1 << BCCParser.T__23))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 198
                self.factor()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_NUM(self):
            return self.getToken(BCCParser.TK_NUM, 0)

        def TK_BOOL(self):
            return self.getToken(BCCParser.TK_BOOL, 0)

        def ID(self):
            return self.getToken(BCCParser.ID, 0)

        def lexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.LexprContext)
            else:
                return self.getTypedRuleContext(BCCParser.LexprContext,i)


        def FID(self):
            return self.getToken(BCCParser.FID, 0)

        def getRuleIndex(self):
            return BCCParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = BCCParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(BCCParser.TK_NUM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(BCCParser.TK_BOOL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 206
                self.match(BCCParser.ID)
                self.state = 207
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 208
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 209
                self.match(BCCParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.match(BCCParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 211
                self.match(BCCParser.T__2)
                self.state = 212
                self.lexpr()
                self.state = 213
                self.match(BCCParser.T__4)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 215
                self.match(BCCParser.FID)
                self.state = 216
                self.match(BCCParser.T__2)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__2) | (1 << BCCParser.T__10) | (1 << BCCParser.T__11) | (1 << BCCParser.FID) | (1 << BCCParser.TK_NUM) | (1 << BCCParser.NOT) | (1 << BCCParser.TK_BOOL) | (1 << BCCParser.ID))) != 0):
                    self.state = 217
                    self.lexpr()
                    self.state = 222
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==BCCParser.T__3:
                        self.state = 218
                        self.match(BCCParser.T__3)
                        self.state = 219
                        self.lexpr()
                        self.state = 224
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 227
                self.match(BCCParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





