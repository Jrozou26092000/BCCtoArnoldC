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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\u00f7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\7\2")
        buf.write("&\n\2\f\2\16\2)\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\7\3\65\n\3\f\3\16\38\13\3\5\3:\n\3\3\3\3\3\7\3")
        buf.write(">\n\3\f\3\16\3A\13\3\3\3\3\3\3\4\7\4F\n\4\f\4\16\4I\13")
        buf.write("\4\3\4\7\4L\n\4\f\4\16\4O\13\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\7\5W\n\5\f\5\16\5Z\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\7\7d\n\7\f\7\16\7g\13\7\3\7\3\7\5\7k\n\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u009f\n\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\5\t\u00a8\n\t\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\5\f\u00b4\n\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\7\r\u00bb\n\r\f\r\16\r\u00be\13\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00c6\n\16\3\17\3\17\3\17\5\17\u00cb\n")
        buf.write("\17\3\20\3\20\3\20\7\20\u00d0\n\20\f\20\16\20\u00d3\13")
        buf.write("\20\3\21\3\21\3\21\7\21\u00d8\n\21\f\21\16\21\u00db\13")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u00ed\n\22\f\22\16")
        buf.write("\22\u00f0\13\22\5\22\u00f2\n\22\3\22\5\22\u00f5\n\22\3")
        buf.write("\22\2\2\23\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"\2")
        buf.write("\7\3\2\r\16\3\2\20\25\3\2\26\33\3\2\34\35\3\2\36 \2\u010a")
        buf.write("\2\'\3\2\2\2\4,\3\2\2\2\6G\3\2\2\2\bR\3\2\2\2\n]\3\2\2")
        buf.write("\2\fj\3\2\2\2\16\u009e\3\2\2\2\20\u00a7\3\2\2\2\22\u00a9")
        buf.write("\3\2\2\2\24\u00ac\3\2\2\2\26\u00b3\3\2\2\2\30\u00b5\3")
        buf.write("\2\2\2\32\u00c5\3\2\2\2\34\u00c7\3\2\2\2\36\u00cc\3\2")
        buf.write("\2\2 \u00d4\3\2\2\2\"\u00f4\3\2\2\2$&\5\4\3\2%$\3\2\2")
        buf.write("\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2)\'\3\2\2")
        buf.write("\2*+\5\6\4\2+\3\3\2\2\2,-\7\3\2\2-.\7#\2\2./\7\4\2\2/")
        buf.write("\60\7\66\2\2\609\7\5\2\2\61\66\5\n\6\2\62\63\7\6\2\2\63")
        buf.write("\65\5\n\6\2\64\62\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66")
        buf.write("\67\3\2\2\2\67:\3\2\2\28\66\3\2\2\29\61\3\2\2\29:\3\2")
        buf.write("\2\2:;\3\2\2\2;?\7\7\2\2<>\5\b\5\2=<\3\2\2\2>A\3\2\2\2")
        buf.write("?=\3\2\2\2?@\3\2\2\2@B\3\2\2\2A?\3\2\2\2BC\5\f\7\2C\5")
        buf.write("\3\2\2\2DF\5\b\5\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2")
        buf.write("\2\2HM\3\2\2\2IG\3\2\2\2JL\5\16\b\2KJ\3\2\2\2LO\3\2\2")
        buf.write("\2MK\3\2\2\2MN\3\2\2\2NP\3\2\2\2OM\3\2\2\2PQ\7\b\2\2Q")
        buf.write("\7\3\2\2\2RS\7\t\2\2SX\5\n\6\2TU\7\6\2\2UW\5\n\6\2VT\3")
        buf.write("\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y[\3\2\2\2ZX\3\2\2")
        buf.write("\2[\\\7\n\2\2\\\t\3\2\2\2]^\7\67\2\2^_\7\4\2\2_`\7\66")
        buf.write("\2\2`\13\3\2\2\2ae\7\13\2\2bd\5\16\b\2cb\3\2\2\2dg\3\2")
        buf.write("\2\2ec\3\2\2\2ef\3\2\2\2fh\3\2\2\2ge\3\2\2\2hk\7\f\2\2")
        buf.write("ik\5\16\b\2ja\3\2\2\2ji\3\2\2\2k\r\3\2\2\2lm\7%\2\2mn")
        buf.write("\5\30\r\2no\7\n\2\2o\u009f\3\2\2\2pq\7&\2\2qr\7\67\2\2")
        buf.write("r\u009f\7\n\2\2st\7\'\2\2tu\5\24\13\2uv\5\22\n\2v\u009f")
        buf.write("\3\2\2\2wx\7(\2\2xy\5\24\13\2yz\5\22\n\2z{\7)\2\2{|\5")
        buf.write("\f\7\2|\u009f\3\2\2\2}~\7*\2\2~\177\5\24\13\2\177\u0080")
        buf.write("\5\22\n\2\u0080\u009f\3\2\2\2\u0081\u0082\5\22\n\2\u0082")
        buf.write("\u0083\7+\2\2\u0083\u0084\5\24\13\2\u0084\u009f\3\2\2")
        buf.write("\2\u0085\u0086\7,\2\2\u0086\u0087\5\30\r\2\u0087\u0088")
        buf.write("\7\n\2\2\u0088\u009f\3\2\2\2\u0089\u008a\7-\2\2\u008a")
        buf.write("\u009f\5\f\7\2\u008b\u008c\7.\2\2\u008c\u008d\7$\2\2\u008d")
        buf.write("\u008e\7\4\2\2\u008e\u009f\5\f\7\2\u008f\u0090\7/\2\2")
        buf.write("\u0090\u0091\7\5\2\2\u0091\u0092\5\30\r\2\u0092\u0093")
        buf.write("\7\n\2\2\u0093\u0094\5\30\r\2\u0094\u0095\7\n\2\2\u0095")
        buf.write("\u0096\5\20\t\2\u0096\u0097\7\7\2\2\u0097\u0098\5\22\n")
        buf.write("\2\u0098\u009f\3\2\2\2\u0099\u009a\7\60\2\2\u009a\u009f")
        buf.write("\7\n\2\2\u009b\u009c\7\61\2\2\u009c\u009f\7\n\2\2\u009d")
        buf.write("\u009f\5\20\t\2\u009el\3\2\2\2\u009ep\3\2\2\2\u009es\3")
        buf.write("\2\2\2\u009ew\3\2\2\2\u009e}\3\2\2\2\u009e\u0081\3\2\2")
        buf.write("\2\u009e\u0085\3\2\2\2\u009e\u0089\3\2\2\2\u009e\u008b")
        buf.write("\3\2\2\2\u009e\u008f\3\2\2\2\u009e\u0099\3\2\2\2\u009e")
        buf.write("\u009b\3\2\2\2\u009e\u009d\3\2\2\2\u009f\17\3\2\2\2\u00a0")
        buf.write("\u00a1\7\67\2\2\u00a1\u00a2\5\26\f\2\u00a2\u00a3\7\n\2")
        buf.write("\2\u00a3\u00a8\3\2\2\2\u00a4\u00a5\t\2\2\2\u00a5\u00a6")
        buf.write("\7\67\2\2\u00a6\u00a8\7\n\2\2\u00a7\u00a0\3\2\2\2\u00a7")
        buf.write("\u00a4\3\2\2\2\u00a8\21\3\2\2\2\u00a9\u00aa\7\17\2\2\u00aa")
        buf.write("\u00ab\5\f\7\2\u00ab\23\3\2\2\2\u00ac\u00ad\7\5\2\2\u00ad")
        buf.write("\u00ae\5\30\r\2\u00ae\u00af\7\7\2\2\u00af\25\3\2\2\2\u00b0")
        buf.write("\u00b1\t\3\2\2\u00b1\u00b4\5\30\r\2\u00b2\u00b4\t\2\2")
        buf.write("\2\u00b3\u00b0\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\27\3")
        buf.write("\2\2\2\u00b5\u00bc\5\32\16\2\u00b6\u00b7\7\62\2\2\u00b7")
        buf.write("\u00bb\5\32\16\2\u00b8\u00b9\7\63\2\2\u00b9\u00bb\5\32")
        buf.write("\16\2\u00ba\u00b6\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00be")
        buf.write("\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\31\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\7\64\2\2\u00c0")
        buf.write("\u00c1\7\5\2\2\u00c1\u00c2\5\30\r\2\u00c2\u00c3\7\7\2")
        buf.write("\2\u00c3\u00c6\3\2\2\2\u00c4\u00c6\5\34\17\2\u00c5\u00bf")
        buf.write("\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\33\3\2\2\2\u00c7\u00ca")
        buf.write("\5\36\20\2\u00c8\u00c9\t\4\2\2\u00c9\u00cb\5\36\20\2\u00ca")
        buf.write("\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\35\3\2\2\2\u00cc")
        buf.write("\u00d1\5 \21\2\u00cd\u00ce\t\5\2\2\u00ce\u00d0\5 \21\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf\3")
        buf.write("\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\37\3\2\2\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d4\u00d9\5\"\22\2\u00d5\u00d6\t\6\2\2\u00d6")
        buf.write("\u00d8\5\"\22\2\u00d7\u00d5\3\2\2\2\u00d8\u00db\3\2\2")
        buf.write("\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da!\3\2")
        buf.write("\2\2\u00db\u00d9\3\2\2\2\u00dc\u00f5\7$\2\2\u00dd\u00f5")
        buf.write("\7\65\2\2\u00de\u00df\7\67\2\2\u00df\u00f5\t\2\2\2\u00e0")
        buf.write("\u00e1\t\2\2\2\u00e1\u00f5\7\67\2\2\u00e2\u00f5\7\67\2")
        buf.write("\2\u00e3\u00e4\7\5\2\2\u00e4\u00e5\5\30\r\2\u00e5\u00e6")
        buf.write("\7\7\2\2\u00e6\u00f5\3\2\2\2\u00e7\u00e8\7#\2\2\u00e8")
        buf.write("\u00f1\7\5\2\2\u00e9\u00ee\5\30\r\2\u00ea\u00eb\7\6\2")
        buf.write("\2\u00eb\u00ed\5\30\r\2\u00ec\u00ea\3\2\2\2\u00ed\u00f0")
        buf.write("\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef")
        buf.write("\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00e9\3\2\2\2")
        buf.write("\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f5\7")
        buf.write("\7\2\2\u00f4\u00dc\3\2\2\2\u00f4\u00dd\3\2\2\2\u00f4\u00de")
        buf.write("\3\2\2\2\u00f4\u00e0\3\2\2\2\u00f4\u00e2\3\2\2\2\u00f4")
        buf.write("\u00e3\3\2\2\2\u00f4\u00e7\3\2\2\2\u00f5#\3\2\2\2\27\'")
        buf.write("\669?GMXej\u009e\u00a7\u00b3\u00ba\u00bc\u00c5\u00ca\u00d1")
        buf.write("\u00d9\u00ee\u00f1\u00f4")
        return buf.getvalue()


class BCCParser ( Parser ):

    grammarFileName = "BCC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "':'", "'('", "','", "')'", 
                     "'end'", "'var'", "';'", "'{'", "'}'", "'--'", "'++'", 
                     "'do'", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'<'", "'=='", "'<='", "'>'", "'>='", "'!='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'print'", "'input'", "'when'", 
                     "'if'", "'else'", "<INVALID>", "<INVALID>", "'return'", 
                     "'loop'", "'repeat'", "'for'", "'next'", "'break'", 
                     "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "COMMENT", 
                      "FID", "TK_NUM", "PRINT", "INPUT", "WHEN", "IF", "ELSE", 
                      "CICLE", "CICLE2", "RETURN", "LOOP", "REPEAT", "FOR", 
                      "NEXT", "BREAK", "AND", "OR", "NOT", "TK_BOOL", "DATATYPE", 
                      "ID" ]

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
    TK_NUM=34
    PRINT=35
    INPUT=36
    WHEN=37
    IF=38
    ELSE=39
    CICLE=40
    CICLE2=41
    RETURN=42
    LOOP=43
    REPEAT=44
    FOR=45
    NEXT=46
    BREAK=47
    AND=48
    OR=49
    NOT=50
    TK_BOOL=51
    DATATYPE=52
    ID=53

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

        def stmt_block(self):
            return self.getTypedRuleContext(BCCParser.Stmt_blockContext,0)


        def var_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.Var_decContext)
            else:
                return self.getTypedRuleContext(BCCParser.Var_decContext,i)


        def stmt_var_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.Stmt_var_listContext)
            else:
                return self.getTypedRuleContext(BCCParser.Stmt_var_listContext,i)


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
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BCCParser.ID:
                self.state = 47
                self.var_dec()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BCCParser.T__3:
                    self.state = 48
                    self.match(BCCParser.T__3)
                    self.state = 49
                    self.var_dec()
                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 57
            self.match(BCCParser.T__4)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__6:
                self.state = 58
                self.stmt_var_list()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
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
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__6:
                self.state = 66
                self.stmt_var_list()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__10) | (1 << BCCParser.T__11) | (1 << BCCParser.T__12) | (1 << BCCParser.PRINT) | (1 << BCCParser.INPUT) | (1 << BCCParser.WHEN) | (1 << BCCParser.IF) | (1 << BCCParser.CICLE) | (1 << BCCParser.RETURN) | (1 << BCCParser.LOOP) | (1 << BCCParser.REPEAT) | (1 << BCCParser.FOR) | (1 << BCCParser.NEXT) | (1 << BCCParser.BREAK) | (1 << BCCParser.ID))) != 0):
                self.state = 72
                self.stmt()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
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
            self.state = 80
            self.match(BCCParser.T__6)
            self.state = 81
            self.var_dec()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__3:
                self.state = 82
                self.match(BCCParser.T__3)
                self.state = 83
                self.var_dec()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
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
            self.state = 91
            self.match(BCCParser.ID)
            self.state = 92
            self.match(BCCParser.T__1)
            self.state = 93
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
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(BCCParser.T__8)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__10) | (1 << BCCParser.T__11) | (1 << BCCParser.T__12) | (1 << BCCParser.PRINT) | (1 << BCCParser.INPUT) | (1 << BCCParser.WHEN) | (1 << BCCParser.IF) | (1 << BCCParser.CICLE) | (1 << BCCParser.RETURN) | (1 << BCCParser.LOOP) | (1 << BCCParser.REPEAT) | (1 << BCCParser.FOR) | (1 << BCCParser.NEXT) | (1 << BCCParser.BREAK) | (1 << BCCParser.ID))) != 0):
                    self.state = 96
                    self.stmt()
                    self.state = 101
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 102
                self.match(BCCParser.T__9)
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11, BCCParser.T__12, BCCParser.PRINT, BCCParser.INPUT, BCCParser.WHEN, BCCParser.IF, BCCParser.CICLE, BCCParser.RETURN, BCCParser.LOOP, BCCParser.REPEAT, BCCParser.FOR, BCCParser.NEXT, BCCParser.BREAK, BCCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
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
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.PRINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(BCCParser.PRINT)
                self.state = 107
                self.lexpr()
                self.state = 108
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.INPUT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(BCCParser.INPUT)
                self.state = 111
                self.match(BCCParser.ID)
                self.state = 112
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.WHEN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.match(BCCParser.WHEN)
                self.state = 114
                self.par_lexpr()
                self.state = 115
                self.do_block()
                pass
            elif token in [BCCParser.IF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 117
                self.match(BCCParser.IF)
                self.state = 118
                self.par_lexpr()
                self.state = 119
                self.do_block()

                self.state = 120
                self.match(BCCParser.ELSE)
                self.state = 121
                self.stmt_block()
                pass
            elif token in [BCCParser.CICLE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 123
                self.match(BCCParser.CICLE)
                self.state = 124
                self.par_lexpr()
                self.state = 125
                self.do_block()
                pass
            elif token in [BCCParser.T__12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 127
                self.do_block()
                self.state = 128
                self.match(BCCParser.CICLE2)
                self.state = 129
                self.par_lexpr()
                pass
            elif token in [BCCParser.RETURN]:
                self.enterOuterAlt(localctx, 7)
                self.state = 131
                self.match(BCCParser.RETURN)
                self.state = 132
                self.lexpr()
                self.state = 133
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.LOOP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 135
                self.match(BCCParser.LOOP)
                self.state = 136
                self.stmt_block()
                pass
            elif token in [BCCParser.REPEAT]:
                self.enterOuterAlt(localctx, 9)
                self.state = 137
                self.match(BCCParser.REPEAT)
                self.state = 138
                self.match(BCCParser.TK_NUM)
                self.state = 139
                self.match(BCCParser.T__1)
                self.state = 140
                self.stmt_block()
                pass
            elif token in [BCCParser.FOR]:
                self.enterOuterAlt(localctx, 10)
                self.state = 141
                self.match(BCCParser.FOR)
                self.state = 142
                self.match(BCCParser.T__2)
                self.state = 143
                self.lexpr()
                self.state = 144
                self.match(BCCParser.T__7)
                self.state = 145
                self.lexpr()
                self.state = 146
                self.match(BCCParser.T__7)
                self.state = 147
                self.assignation()
                self.state = 148
                self.match(BCCParser.T__4)
                self.state = 149
                self.do_block()
                pass
            elif token in [BCCParser.NEXT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 151
                self.match(BCCParser.NEXT)
                self.state = 152
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.BREAK]:
                self.enterOuterAlt(localctx, 12)
                self.state = 153
                self.match(BCCParser.BREAK)
                self.state = 154
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11, BCCParser.ID]:
                self.enterOuterAlt(localctx, 13)
                self.state = 155
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
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(BCCParser.ID)
                self.state = 159
                self.operation()
                self.state = 160
                self.match(BCCParser.T__7)
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
                self.match(BCCParser.ID)
                self.state = 164
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
            self.state = 167
            self.match(BCCParser.T__12)
            self.state = 168
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
            self.state = 170
            self.match(BCCParser.T__2)
            self.state = 171
            self.lexpr()
            self.state = 172
            self.match(BCCParser.T__4)
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
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.T__13, BCCParser.T__14, BCCParser.T__15, BCCParser.T__16, BCCParser.T__17, BCCParser.T__18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__13) | (1 << BCCParser.T__14) | (1 << BCCParser.T__15) | (1 << BCCParser.T__16) | (1 << BCCParser.T__17) | (1 << BCCParser.T__18))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 175
                self.lexpr()
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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
            self.state = 179
            self.nexpr()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.AND or _la==BCCParser.OR:
                self.state = 184
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BCCParser.AND]:
                    self.state = 180
                    self.match(BCCParser.AND)
                    self.state = 181
                    self.nexpr()
                    pass
                elif token in [BCCParser.OR]:
                    self.state = 182
                    self.match(BCCParser.OR)
                    self.state = 183
                    self.nexpr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 188
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
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(BCCParser.NOT)
                self.state = 190
                self.match(BCCParser.T__2)
                self.state = 191
                self.lexpr()
                self.state = 192
                self.match(BCCParser.T__4)
                pass
            elif token in [BCCParser.T__2, BCCParser.T__10, BCCParser.T__11, BCCParser.FID, BCCParser.TK_NUM, BCCParser.TK_BOOL, BCCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
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
            self.state = 197
            self.simple_expr()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__19) | (1 << BCCParser.T__20) | (1 << BCCParser.T__21) | (1 << BCCParser.T__22) | (1 << BCCParser.T__23) | (1 << BCCParser.T__24))) != 0):
                self.state = 198
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__19) | (1 << BCCParser.T__20) | (1 << BCCParser.T__21) | (1 << BCCParser.T__22) | (1 << BCCParser.T__23) | (1 << BCCParser.T__24))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 199
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
            self.state = 202
            self.term()
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__25 or _la==BCCParser.T__26:
                self.state = 203
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__25 or _la==BCCParser.T__26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 204
                self.term()
                self.state = 209
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
            self.state = 210
            self.factor()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__27) | (1 << BCCParser.T__28) | (1 << BCCParser.T__29))) != 0):
                self.state = 211
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__27) | (1 << BCCParser.T__28) | (1 << BCCParser.T__29))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 212
                self.factor()
                self.state = 217
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
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(BCCParser.TK_NUM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(BCCParser.TK_BOOL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.match(BCCParser.ID)
                self.state = 221
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.match(BCCParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 224
                self.match(BCCParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 225
                self.match(BCCParser.T__2)
                self.state = 226
                self.lexpr()
                self.state = 227
                self.match(BCCParser.T__4)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 229
                self.match(BCCParser.FID)
                self.state = 230
                self.match(BCCParser.T__2)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__2) | (1 << BCCParser.T__10) | (1 << BCCParser.T__11) | (1 << BCCParser.FID) | (1 << BCCParser.TK_NUM) | (1 << BCCParser.NOT) | (1 << BCCParser.TK_BOOL) | (1 << BCCParser.ID))) != 0):
                    self.state = 231
                    self.lexpr()
                    self.state = 236
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==BCCParser.T__3:
                        self.state = 232
                        self.match(BCCParser.T__3)
                        self.state = 233
                        self.lexpr()
                        self.state = 238
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 241
                self.match(BCCParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





