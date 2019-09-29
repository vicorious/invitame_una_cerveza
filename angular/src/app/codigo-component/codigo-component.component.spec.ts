import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CodigoComponentComponent } from './codigo-component.component';

describe('CodigoComponentComponent', () => {
  let component: CodigoComponentComponent;
  let fixture: ComponentFixture<CodigoComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CodigoComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CodigoComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
