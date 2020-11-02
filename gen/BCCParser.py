# Generated from /home/juanr/Semestre 2020-2/Lenguajes de Programación/TraductorArnoldC/grammar/BCC.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\u00e8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\7\2")
        buf.write("&\n\2\f\2\16\2)\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\7\48\n\4\f\4\16\4;\13\4\3\4\7\4>\n")
        buf.write("\4\f\4\16\4A\13\4\3\4\3\4\3\5\3\5\3\5\7\5H\n\5\f\5\16")
        buf.write("\5K\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\7\7V\n\7")
        buf.write("\f\7\16\7Y\13\7\3\7\3\7\5\7]\n\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u0091\n\b\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u0098\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\5\f\u00a7\n\f\3\r\3\r\3\r\3\r\3\r\7\r\u00ae")
        buf.write("\n\r\f\r\16\r\u00b1\13\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00b9\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\7")
        buf.write("\20\u00c2\n\20\f\20\16\20\u00c5\13\20\3\21\3\21\3\21\7")
        buf.write("\21\u00ca\n\21\f\21\16\21\u00cd\13\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\7\22\u00df\n\22\f\22\16\22\u00e2\13\22\3\22")
        buf.write("\3\22\5\22\u00e6\n\22\3\22\2\2\23\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"\2\7\3\2\r\16\3\2\20\25\3\2\26\33")
        buf.write("\3\2\34\35\3\2\36 \2\u00f6\2\'\3\2\2\2\4,\3\2\2\2\69\3")
        buf.write("\2\2\2\bD\3\2\2\2\nN\3\2\2\2\f\\\3\2\2\2\16\u0090\3\2")
        buf.write("\2\2\20\u0097\3\2\2\2\22\u0099\3\2\2\2\24\u009c\3\2\2")
        buf.write("\2\26\u00a6\3\2\2\2\30\u00a8\3\2\2\2\32\u00b8\3\2\2\2")
        buf.write("\34\u00ba\3\2\2\2\36\u00be\3\2\2\2 \u00c6\3\2\2\2\"\u00e5")
        buf.write("\3\2\2\2$&\5\4\3\2%$\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3")
        buf.write("\2\2\2(*\3\2\2\2)\'\3\2\2\2*+\5\6\4\2+\3\3\2\2\2,-\7\3")
        buf.write("\2\2-.\7#\2\2./\7\4\2\2/\60\7\67\2\2\60\61\7\5\2\2\61")
        buf.write("\62\5\n\6\2\62\63\7\6\2\2\63\64\5\b\5\2\64\65\5\f\7\2")
        buf.write("\65\5\3\2\2\2\668\5\b\5\2\67\66\3\2\2\28;\3\2\2\29\67")
        buf.write("\3\2\2\29:\3\2\2\2:?\3\2\2\2;9\3\2\2\2<>\5\16\b\2=<\3")
        buf.write("\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@B\3\2\2\2A?\3\2\2")
        buf.write("\2BC\7\7\2\2C\7\3\2\2\2DI\5\n\6\2EF\7\b\2\2FH\5\n\6\2")
        buf.write("GE\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KI\3")
        buf.write("\2\2\2LM\7\t\2\2M\t\3\2\2\2NO\7\n\2\2OP\7$\2\2PQ\7\4\2")
        buf.write("\2QR\7\67\2\2R\13\3\2\2\2SW\7\13\2\2TV\5\16\b\2UT\3\2")
        buf.write("\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2YW\3\2\2\2")
        buf.write("Z]\7\f\2\2[]\5\16\b\2\\S\3\2\2\2\\[\3\2\2\2]\r\3\2\2\2")
        buf.write("^_\7&\2\2_`\5\30\r\2`a\7\t\2\2a\u0091\3\2\2\2bc\7\'\2")
        buf.write("\2cd\7$\2\2d\u0091\7\t\2\2ef\7(\2\2fg\5\24\13\2gh\5\22")
        buf.write("\n\2h\u0091\3\2\2\2ij\7)\2\2jk\5\24\13\2kl\5\22\n\2lm")
        buf.write("\7*\2\2mn\5\f\7\2n\u0091\3\2\2\2op\7+\2\2pq\5\24\13\2")
        buf.write("qr\5\22\n\2r\u0091\3\2\2\2st\5\22\n\2tu\7,\2\2uv\5\24")
        buf.write("\13\2v\u0091\3\2\2\2wx\7-\2\2xy\5\30\r\2yz\7\t\2\2z\u0091")
        buf.write("\3\2\2\2{|\7.\2\2|\u0091\5\f\7\2}~\7/\2\2~\177\7%\2\2")
        buf.write("\177\u0080\7\4\2\2\u0080\u0091\5\f\7\2\u0081\u0082\7\60")
        buf.write("\2\2\u0082\u0083\7\5\2\2\u0083\u0084\5\30\r\2\u0084\u0085")
        buf.write("\7\t\2\2\u0085\u0086\5\30\r\2\u0086\u0087\7\t\2\2\u0087")
        buf.write("\u0088\5\20\t\2\u0088\u0089\7\6\2\2\u0089\u008a\5\22\n")
        buf.write("\2\u008a\u0091\3\2\2\2\u008b\u008c\7\61\2\2\u008c\u0091")
        buf.write("\7\t\2\2\u008d\u008e\7\62\2\2\u008e\u0091\7\t\2\2\u008f")
        buf.write("\u0091\5\20\t\2\u0090^\3\2\2\2\u0090b\3\2\2\2\u0090e\3")
        buf.write("\2\2\2\u0090i\3\2\2\2\u0090o\3\2\2\2\u0090s\3\2\2\2\u0090")
        buf.write("w\3\2\2\2\u0090{\3\2\2\2\u0090}\3\2\2\2\u0090\u0081\3")
        buf.write("\2\2\2\u0090\u008b\3\2\2\2\u0090\u008d\3\2\2\2\u0090\u008f")
        buf.write("\3\2\2\2\u0091\17\3\2\2\2\u0092\u0093\7$\2\2\u0093\u0098")
        buf.write("\5\26\f\2\u0094\u0095\t\2\2\2\u0095\u0096\7$\2\2\u0096")
        buf.write("\u0098\7\t\2\2\u0097\u0092\3\2\2\2\u0097\u0094\3\2\2\2")
        buf.write("\u0098\21\3\2\2\2\u0099\u009a\7\17\2\2\u009a\u009b\5\f")
        buf.write("\7\2\u009b\23\3\2\2\2\u009c\u009d\7\5\2\2\u009d\u009e")
        buf.write("\5\30\r\2\u009e\u009f\7\6\2\2\u009f\25\3\2\2\2\u00a0\u00a1")
        buf.write("\t\3\2\2\u00a1\u00a2\5\30\r\2\u00a2\u00a3\7\t\2\2\u00a3")
        buf.write("\u00a7\3\2\2\2\u00a4\u00a5\t\2\2\2\u00a5\u00a7\7\t\2\2")
        buf.write("\u00a6\u00a0\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\27\3\2")
        buf.write("\2\2\u00a8\u00af\5\32\16\2\u00a9\u00aa\7\63\2\2\u00aa")
        buf.write("\u00ae\5\32\16\2\u00ab\u00ac\7\64\2\2\u00ac\u00ae\5\32")
        buf.write("\16\2\u00ad\u00a9\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b1")
        buf.write("\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0")
        buf.write("\31\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b3\7\65\2\2\u00b3")
        buf.write("\u00b4\7\5\2\2\u00b4\u00b5\5\30\r\2\u00b5\u00b6\7\6\2")
        buf.write("\2\u00b6\u00b9\3\2\2\2\u00b7\u00b9\5\34\17\2\u00b8\u00b2")
        buf.write("\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\33\3\2\2\2\u00ba\u00bb")
        buf.write("\5\36\20\2\u00bb\u00bc\t\4\2\2\u00bc\u00bd\5\36\20\2\u00bd")
        buf.write("\35\3\2\2\2\u00be\u00c3\5 \21\2\u00bf\u00c0\t\5\2\2\u00c0")
        buf.write("\u00c2\5 \21\2\u00c1\u00bf\3\2\2\2\u00c2\u00c5\3\2\2\2")
        buf.write("\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\37\3\2")
        buf.write("\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00cb\5\"\22\2\u00c7\u00c8")
        buf.write("\t\6\2\2\u00c8\u00ca\5\"\22\2\u00c9\u00c7\3\2\2\2\u00ca")
        buf.write("\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2")
        buf.write("\u00cc!\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00e6\7%\2\2")
        buf.write("\u00cf\u00e6\7\66\2\2\u00d0\u00d1\7$\2\2\u00d1\u00e6\t")
        buf.write("\2\2\2\u00d2\u00d3\t\2\2\2\u00d3\u00e6\7$\2\2\u00d4\u00e6")
        buf.write("\7$\2\2\u00d5\u00d6\7\5\2\2\u00d6\u00d7\5\30\r\2\u00d7")
        buf.write("\u00d8\7\6\2\2\u00d8\u00e6\3\2\2\2\u00d9\u00da\7#\2\2")
        buf.write("\u00da\u00db\7\5\2\2\u00db\u00e0\5\30\r\2\u00dc\u00dd")
        buf.write("\7\b\2\2\u00dd\u00df\5\30\r\2\u00de\u00dc\3\2\2\2\u00df")
        buf.write("\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e3\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\7")
        buf.write("\6\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00ce\3\2\2\2\u00e5\u00cf")
        buf.write("\3\2\2\2\u00e5\u00d0\3\2\2\2\u00e5\u00d2\3\2\2\2\u00e5")
        buf.write("\u00d4\3\2\2\2\u00e5\u00d5\3\2\2\2\u00e5\u00d9\3\2\2\2")
        buf.write("\u00e6#\3\2\2\2\22\'9?IW\\\u0090\u0097\u00a6\u00ad\u00af")
        buf.write("\u00b8\u00c3\u00cb\u00e0\u00e5")
        return buf.getvalue()


class BCCParser ( Parser ):

    grammarFileName = "BCC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "':'", "'('", "')'", "'end'", 
                     "','", "';'", "'var'", "'{'", "'}'", "'--'", "'++'", 
                     "'do'", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'<'", "'=='", "'<='", "'>'", "'>='", "'!='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "<INVALID>", "<INVALID>", 
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
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "COMMENT", 
                      "FID", "ID", "TK_NUM", "PRINT", "INPUT", "WHEN", "IF", 
                      "ELSE", "CICLE", "CICLE2", "RETURN", "LOOP", "REPEAT", 
                      "FOR", "NEXT", "BREAK", "AND", "OR", "NOT", "TK_BOOL", 
                      "DATATYPE" ]

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
    RULE_operation = 10
    RULE_lexpr = 11
    RULE_nexpr = 12
    RULE_rexpr = 13
    RULE_simple_expr = 14
    RULE_term = 15
    RULE_factor = 16

    ruleNames =  [ "prog", "f", "main_prog", "stmt_var_list", "var_dec", 
                   "stmt_block", "stmt", "assignation", "do_block", "par_lexpr", 
                   "operation", "lexpr", "nexpr", "rexpr", "simple_expr", 
                   "term", "factor" ]

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
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    WS=31
    COMMENT=32
    FID=33
    ID=34
    TK_NUM=35
    PRINT=36
    INPUT=37
    WHEN=38
    IF=39
    ELSE=40
    CICLE=41
    CICLE2=42
    RETURN=43
    LOOP=44
    REPEAT=45
    FOR=46
    NEXT=47
    BREAK=48
    AND=49
    OR=50
    NOT=51
    TK_BOOL=52
    DATATYPE=53

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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__0:
                self.state = 34
                self.f()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
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

        def var_dec(self):
            return self.getTypedRuleContext(BCCParser.Var_decContext,0)


        def stmt_var_list(self):
            return self.getTypedRuleContext(BCCParser.Stmt_var_listContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(BCCParser.Stmt_blockContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(BCCParser.T__0)
            self.state = 43
            self.match(BCCParser.FID)
            self.state = 44
            self.match(BCCParser.T__1)
            self.state = 45
            self.match(BCCParser.DATATYPE)
            self.state = 46
            self.match(BCCParser.T__2)
            self.state = 47
            self.var_dec()
            self.state = 48
            self.match(BCCParser.T__3)
            self.state = 49
            self.stmt_var_list()
            self.state = 50
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

        def stmt_var_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.Stmt_var_listContext)
            else:
                return self.getTypedRuleContext(BCCParser.Stmt_var_listContext,i)


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
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__7:
                self.state = 52
                self.stmt_var_list()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__10) | (1 << BCCParser.T__11) | (1 << BCCParser.T__12) | (1 << BCCParser.ID) | (1 << BCCParser.PRINT) | (1 << BCCParser.INPUT) | (1 << BCCParser.WHEN) | (1 << BCCParser.IF) | (1 << BCCParser.CICLE) | (1 << BCCParser.RETURN) | (1 << BCCParser.LOOP) | (1 << BCCParser.REPEAT) | (1 << BCCParser.FOR) | (1 << BCCParser.NEXT) | (1 << BCCParser.BREAK))) != 0):
                self.state = 58
                self.stmt()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(BCCParser.T__4)
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
            self.state = 66
            self.var_dec()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__5:
                self.state = 67
                self.match(BCCParser.T__5)
                self.state = 68
                self.var_dec()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(BCCParser.T__6)
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
            self.state = 76
            self.match(BCCParser.T__7)
            self.state = 77
            self.match(BCCParser.ID)
            self.state = 78
            self.match(BCCParser.T__1)
            self.state = 79
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
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(BCCParser.T__8)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__10) | (1 << BCCParser.T__11) | (1 << BCCParser.T__12) | (1 << BCCParser.ID) | (1 << BCCParser.PRINT) | (1 << BCCParser.INPUT) | (1 << BCCParser.WHEN) | (1 << BCCParser.IF) | (1 << BCCParser.CICLE) | (1 << BCCParser.RETURN) | (1 << BCCParser.LOOP) | (1 << BCCParser.REPEAT) | (1 << BCCParser.FOR) | (1 << BCCParser.NEXT) | (1 << BCCParser.BREAK))) != 0):
                    self.state = 82
                    self.stmt()
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 88
                self.match(BCCParser.T__9)
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11, BCCParser.T__12, BCCParser.ID, BCCParser.PRINT, BCCParser.INPUT, BCCParser.WHEN, BCCParser.IF, BCCParser.CICLE, BCCParser.RETURN, BCCParser.LOOP, BCCParser.REPEAT, BCCParser.FOR, BCCParser.NEXT, BCCParser.BREAK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
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
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.PRINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(BCCParser.PRINT)
                self.state = 93
                self.lexpr()
                self.state = 94
                self.match(BCCParser.T__6)
                pass
            elif token in [BCCParser.INPUT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(BCCParser.INPUT)
                self.state = 97
                self.match(BCCParser.ID)
                self.state = 98
                self.match(BCCParser.T__6)
                pass
            elif token in [BCCParser.WHEN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                self.match(BCCParser.WHEN)
                self.state = 100
                self.par_lexpr()
                self.state = 101
                self.do_block()
                pass
            elif token in [BCCParser.IF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 103
                self.match(BCCParser.IF)
                self.state = 104
                self.par_lexpr()
                self.state = 105
                self.do_block()

                self.state = 106
                self.match(BCCParser.ELSE)
                self.state = 107
                self.stmt_block()
                pass
            elif token in [BCCParser.CICLE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 109
                self.match(BCCParser.CICLE)
                self.state = 110
                self.par_lexpr()
                self.state = 111
                self.do_block()
                pass
            elif token in [BCCParser.T__12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 113
                self.do_block()
                self.state = 114
                self.match(BCCParser.CICLE2)
                self.state = 115
                self.par_lexpr()
                pass
            elif token in [BCCParser.RETURN]:
                self.enterOuterAlt(localctx, 7)
                self.state = 117
                self.match(BCCParser.RETURN)
                self.state = 118
                self.lexpr()
                self.state = 119
                self.match(BCCParser.T__6)
                pass
            elif token in [BCCParser.LOOP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 121
                self.match(BCCParser.LOOP)
                self.state = 122
                self.stmt_block()
                pass
            elif token in [BCCParser.REPEAT]:
                self.enterOuterAlt(localctx, 9)
                self.state = 123
                self.match(BCCParser.REPEAT)
                self.state = 124
                self.match(BCCParser.TK_NUM)
                self.state = 125
                self.match(BCCParser.T__1)
                self.state = 126
                self.stmt_block()
                pass
            elif token in [BCCParser.FOR]:
                self.enterOuterAlt(localctx, 10)
                self.state = 127
                self.match(BCCParser.FOR)
                self.state = 128
                self.match(BCCParser.T__2)
                self.state = 129
                self.lexpr()
                self.state = 130
                self.match(BCCParser.T__6)
                self.state = 131
                self.lexpr()
                self.state = 132
                self.match(BCCParser.T__6)
                self.state = 133
                self.assignation()
                self.state = 134
                self.match(BCCParser.T__3)
                self.state = 135
                self.do_block()
                pass
            elif token in [BCCParser.NEXT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 137
                self.match(BCCParser.NEXT)
                self.state = 138
                self.match(BCCParser.T__6)
                pass
            elif token in [BCCParser.BREAK]:
                self.enterOuterAlt(localctx, 12)
                self.state = 139
                self.match(BCCParser.BREAK)
                self.state = 140
                self.match(BCCParser.T__6)
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11, BCCParser.ID]:
                self.enterOuterAlt(localctx, 13)
                self.state = 141
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

        def operation(self):
            return self.getTypedRuleContext(BCCParser.OperationContext,0)


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
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(BCCParser.ID)
                self.state = 145
                self.operation()
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 147
                self.match(BCCParser.ID)
                self.state = 148
                self.match(BCCParser.T__6)
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
            self.state = 151
            self.match(BCCParser.T__12)
            self.state = 152
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
            self.state = 154
            self.match(BCCParser.T__2)
            self.state = 155
            self.lexpr()
            self.state = 156
            self.match(BCCParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexpr(self):
            return self.getTypedRuleContext(BCCParser.LexprContext,0)


        def getRuleIndex(self):
            return BCCParser.RULE_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = BCCParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.T__13, BCCParser.T__14, BCCParser.T__15, BCCParser.T__16, BCCParser.T__17, BCCParser.T__18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__13) | (1 << BCCParser.T__14) | (1 << BCCParser.T__15) | (1 << BCCParser.T__16) | (1 << BCCParser.T__17) | (1 << BCCParser.T__18))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 159
                self.lexpr()
                self.state = 160
                self.match(BCCParser.T__6)
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                self.match(BCCParser.T__6)
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
        self.enterRule(localctx, 22, self.RULE_lexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.nexpr()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.AND or _la==BCCParser.OR:
                self.state = 171
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BCCParser.AND]:
                    self.state = 167
                    self.match(BCCParser.AND)
                    self.state = 168
                    self.nexpr()
                    pass
                elif token in [BCCParser.OR]:
                    self.state = 169
                    self.match(BCCParser.OR)
                    self.state = 170
                    self.nexpr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 175
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
        self.enterRule(localctx, 24, self.RULE_nexpr)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(BCCParser.NOT)
                self.state = 177
                self.match(BCCParser.T__2)
                self.state = 178
                self.lexpr()
                self.state = 179
                self.match(BCCParser.T__3)
                pass
            elif token in [BCCParser.T__2, BCCParser.T__10, BCCParser.T__11, BCCParser.FID, BCCParser.ID, BCCParser.TK_NUM, BCCParser.TK_BOOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
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
        self.enterRule(localctx, 26, self.RULE_rexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.simple_expr()

            self.state = 185
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__19) | (1 << BCCParser.T__20) | (1 << BCCParser.T__21) | (1 << BCCParser.T__22) | (1 << BCCParser.T__23) | (1 << BCCParser.T__24))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 186
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
        self.enterRule(localctx, 28, self.RULE_simple_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.term()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__25 or _la==BCCParser.T__26:
                self.state = 189
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__25 or _la==BCCParser.T__26):
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
        self.enterRule(localctx, 30, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.factor()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__27) | (1 << BCCParser.T__28) | (1 << BCCParser.T__29))) != 0):
                self.state = 197
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__27) | (1 << BCCParser.T__28) | (1 << BCCParser.T__29))) != 0)):
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
        self.enterRule(localctx, 32, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
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
                self.match(BCCParser.T__3)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 215
                self.match(BCCParser.FID)
                self.state = 216
                self.match(BCCParser.T__2)

                self.state = 217
                self.lexpr()
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BCCParser.T__5:
                    self.state = 218
                    self.match(BCCParser.T__5)
                    self.state = 219
                    self.lexpr()
                    self.state = 224
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 225
                self.match(BCCParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





